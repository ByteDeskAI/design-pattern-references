"""Minimal stdio MCP server for the design-pattern catalog."""

from __future__ import annotations

import json
import sys
from typing import Any

from pattern_context import context_pack, decision_simulation, migration_plan, snippet_matches
from pattern_graph import catalog_graph, graph_query
from pattern_intelligence import adr_payload, recommend_entries
from pattern_scanner import scan_path


SERVER_INFO = {"name": "design-patterns", "version": "0.8.2"}


SLASH_COMMAND_EXAMPLES: list[dict[str, Any]] = [
    {
        "command": '/patterns-recommend "add a new SCM provider without changing rule execution code" --language python --scope backend --limit 5',
        "tool": "patterns_recommend",
        "arguments": {
            "query": "add a new SCM provider without changing rule execution code",
            "language": "python",
            "scope": "backend",
            "limit": 5,
        },
    },
    {
        "command": '/patterns-scan backend/app/workflow_engine --min-confidence 0.45',
        "tool": "patterns_scan",
        "arguments": {"path": "backend/app/workflow_engine", "min_confidence": 0.45},
    },
    {
        "command": '/patterns-context backend/app/providers/ai --query "adding a new AI provider safely" --language python --scope backend',
        "tool": "patterns_context",
        "arguments": {
            "path": "backend/app/providers/ai",
            "query": "adding a new AI provider safely",
            "language": "python",
            "scope": "backend",
        },
    },
    {
        "command": '/patterns-simulate "Strategy vs Chain of Responsibility for AI provider failover" --language python --risk operability',
        "tool": "patterns_simulate",
        "arguments": {
            "query": "Strategy vs Chain of Responsibility for AI provider failover",
            "language": "python",
            "risk": "operability",
        },
    },
    {
        "command": '/patterns-migrate "hardcoded if/elif provider selection" --to strategy --language python',
        "tool": "patterns_migrate",
        "arguments": {
            "source": "hardcoded if/elif provider selection",
            "target": "strategy",
            "language": "python",
        },
    },
    {
        "command": '/patterns-snippets strategy,idempotent-receiver --language python',
        "tool": "patterns_snippets",
        "arguments": {"patterns": ["strategy", "idempotent-receiver"], "language": "python"},
    },
    {
        "command": '/patterns-adr "durable event storage for SSE replay: Redis vs PostgreSQL" --language python --scope backend',
        "tool": "patterns_adr",
        "arguments": {
            "query": "durable event storage for SSE replay: Redis vs PostgreSQL",
            "language": "python",
            "scope": "backend",
        },
    },
    {
        "command": '/patterns-graph "what patterns mitigate naive exactly once"',
        "tool": "patterns_graph",
        "arguments": {"query": "what patterns mitigate naive exactly once"},
    },
]


def tool_definitions() -> list[dict[str, Any]]:
    string_schema = {"type": "string"}
    return [
        {
            "name": "patterns_recommend",
            "description": 'Recommend catalog patterns, playbooks, recipes, and smells for an architecture force. User slash command: /patterns-recommend "<query>" [--language python] [--scope backend] [--limit 5].',
            "inputSchema": {
                "type": "object",
                "properties": {
                    "query": string_schema,
                    "scope": string_schema,
                    "language": string_schema,
                    "risk": string_schema,
                    "limit": {"type": "integer"},
                },
                "required": ["query"],
            },
        },
        {
            "name": "patterns_scan",
            "description": "Scan a repository path or file for pattern-relevant architecture smells. User slash command: /patterns-scan <path> [--min-confidence 0.45] [--include-docs].",
            "inputSchema": {
                "type": "object",
                "properties": {
                    "path": string_schema,
                    "pack": string_schema,
                    "include_docs": {"type": "boolean"},
                    "include_generated": {"type": "boolean"},
                    "min_confidence": {"type": "number"},
                },
                "required": ["path"],
            },
        },
        {
            "name": "patterns_adr",
            "description": 'Generate an ADR-style catalog-backed architecture decision seed. User slash command: /patterns-adr "<decision>" [--language python] [--scope backend].',
            "inputSchema": {
                "type": "object",
                "properties": {"query": string_schema, "language": string_schema, "scope": string_schema, "status": string_schema},
                "required": ["query"],
            },
        },
        {
            "name": "patterns_context",
            "description": 'Build a model-ready context pack with scan findings, recommendations, snippets, and ADR seed. User slash command: /patterns-context <path> --query "<problem>" [--language python].',
            "inputSchema": {
                "type": "object",
                "properties": {"path": string_schema, "query": string_schema, "language": string_schema, "scope": string_schema},
                "required": ["path", "query"],
            },
        },
        {
            "name": "patterns_graph",
            "description": 'Return the typed catalog graph or answer graph relationship questions. User slash command: /patterns-graph ["relationship question"].',
            "inputSchema": {
                "type": "object",
                "properties": {"query": string_schema, "format": string_schema},
            },
        },
        {
            "name": "patterns_simulate",
            "description": 'Score likely pattern options against the architecture decision scorecard. User slash command: /patterns-simulate "<decision>" [--language python] [--risk operability].',
            "inputSchema": {
                "type": "object",
                "properties": {"query": string_schema, "language": string_schema, "risk": string_schema, "limit": {"type": "integer"}},
                "required": ["query"],
            },
        },
        {
            "name": "patterns_migrate",
            "description": 'Create a recipe-backed migration plan from a smell/current shape to a target pattern. User slash command: /patterns-migrate "<current smell>" --to <target-pattern> [--language python].',
            "inputSchema": {
                "type": "object",
                "properties": {"source": string_schema, "target": string_schema, "language": string_schema, "query": string_schema},
                "required": ["source", "target"],
            },
        },
        {
            "name": "patterns_snippets",
            "description": "Return language-specific implementation snippets for catalog pattern slugs. User slash command: /patterns-snippets strategy,idempotent-receiver [--language python].",
            "inputSchema": {
                "type": "object",
                "properties": {
                    "patterns": {"type": "array", "items": string_schema},
                    "language": string_schema,
                },
                "required": ["patterns"],
            },
        },
        {
            "name": "patterns_examples",
            "description": "Return copyable /patterns-* slash-command examples for the design-patterns plugin. Use this when a user asks for example MCP requests or how to call the design patterns tool.",
            "inputSchema": {
                "type": "object",
                "properties": {"topic": string_schema},
            },
        },
    ]


def _json_text(value: Any) -> dict[str, str]:
    return {"type": "text", "text": json.dumps(value, indent=2, sort_keys=True)}


def call_tool(name: str, arguments: dict[str, Any]) -> Any:
    if name == "patterns_examples":
        topic = str(arguments.get("topic", "")).strip()
        return {
            "usage": "When users ask for example MCP requests, lead with these copyable slash commands instead of describing tool schemas.",
            "format": '/patterns-<action> <required-argument> [--optional-flag value]',
            "topic": topic or "all",
            "slashCommands": SLASH_COMMAND_EXAMPLES,
        }
    if name == "patterns_recommend":
        return recommend_entries(
            str(arguments.get("query", "")),
            scope=str(arguments.get("scope", "all")),
            language=arguments.get("language") or None,
            risk=str(arguments.get("risk", "balanced")),
            limit=int(arguments.get("limit", 8)),
            include_snippets=True,
        )
    if name == "patterns_scan":
        return scan_path(
            str(arguments.get("path", ".")),
            pack=str(arguments.get("pack", "all")),
            include_docs=bool(arguments.get("include_docs", False)),
            include_generated=bool(arguments.get("include_generated", False)),
            min_confidence=float(arguments.get("min_confidence", 0.0)),
        )
    if name == "patterns_adr":
        return adr_payload(
            str(arguments.get("query", "")),
            status=str(arguments.get("status", "Proposed")),
            language=arguments.get("language") or None,
            scope=str(arguments.get("scope", "all")),
        )
    if name == "patterns_context":
        return context_pack(
            str(arguments.get("path", ".")),
            str(arguments.get("query", "")),
            language=arguments.get("language") or None,
            scope=str(arguments.get("scope", "all")),
        )
    if name == "patterns_graph":
        query = str(arguments.get("query", "")).strip()
        return graph_query(query) if query else catalog_graph()
    if name == "patterns_simulate":
        return decision_simulation(
            str(arguments.get("query", "")),
            language=arguments.get("language") or None,
            risk=str(arguments.get("risk", "balanced")),
            limit=int(arguments.get("limit", 5)),
        )
    if name == "patterns_migrate":
        return migration_plan(
            str(arguments.get("source", "")),
            str(arguments.get("target", "")),
            language=arguments.get("language") or None,
            query=str(arguments.get("query", "")),
        )
    if name == "patterns_snippets":
        return snippet_matches(set(arguments.get("patterns", [])), arguments.get("language") or None)
    raise ValueError(f"Unknown tool: {name}")


def handle_request(request: dict[str, Any]) -> dict[str, Any] | None:
    method = request.get("method")
    request_id = request.get("id")
    try:
        if method == "initialize":
            return {
                "jsonrpc": "2.0",
                "id": request_id,
                "result": {
                    "protocolVersion": "2025-03-26",
                    "capabilities": {"tools": {}},
                    "serverInfo": SERVER_INFO,
                },
            }
        if method == "notifications/initialized":
            return None
        if method == "tools/list":
            return {"jsonrpc": "2.0", "id": request_id, "result": {"tools": tool_definitions()}}
        if method == "tools/call":
            params = request.get("params", {})
            result = call_tool(str(params.get("name", "")), dict(params.get("arguments", {})))
            return {"jsonrpc": "2.0", "id": request_id, "result": {"content": [_json_text(result)]}}
        return {
            "jsonrpc": "2.0",
            "id": request_id,
            "error": {"code": -32601, "message": f"Method not found: {method}"},
        }
    except Exception as exc:  # noqa: BLE001 - JSON-RPC servers should return protocol errors.
        return {
            "jsonrpc": "2.0",
            "id": request_id,
            "error": {"code": -32000, "message": str(exc)},
        }


def serve_stdio() -> int:
    for line in sys.stdin:
        if not line.strip():
            continue
        try:
            request = json.loads(line)
        except json.JSONDecodeError as exc:
            response = {"jsonrpc": "2.0", "id": None, "error": {"code": -32700, "message": str(exc)}}
        else:
            response = handle_request(request)
        if response is not None:
            sys.stdout.write(json.dumps(response, separators=(",", ":")) + "\n")
            sys.stdout.flush()
    return 0


def main() -> int:
    return serve_stdio()


if __name__ == "__main__":
    raise SystemExit(main())
