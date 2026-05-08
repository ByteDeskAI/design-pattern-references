"""Minimal stdio MCP server for the design-pattern catalog."""

from __future__ import annotations

import json
import sys
from typing import Any

from pattern_context import context_pack, decision_simulation, migration_plan, snippet_matches
from pattern_graph import catalog_graph, graph_query
from pattern_inference import infer_request_context
from pattern_intelligence import adr_payload, recommend_entries
from pattern_scanner import scan_path


SERVER_INFO = {"name": "design-patterns", "version": "0.8.4"}


SLASH_COMMAND_HELP: dict[str, dict[str, Any]] = {
    "patterns-recommend": {
        "tool": "patterns_recommend",
        "purpose": "Recommend patterns, playbooks, recipes, and smells for an architecture force or problem.",
        "usage": '/patterns-recommend "<query>" [--language <language>] [--scope <scope>] [--risk <risk>] [--limit <n>]',
        "helpCommand": "/patterns-recommend help",
        "options": [
            "--language <language>: optional; inferred from codebase and prompt context when omitted.",
            "--scope <scope>: optional; inferred as object-design, integration-design, a catalog domain, or all when omitted.",
            "--risk <risk>: bias recommendations toward balanced, operability, simplicity, or similar decision forces.",
            "--limit <n>: maximum recommendation count.",
        ],
        "examples": [
            '/patterns-recommend "add a new SCM provider without changing rule execution code" --limit 5',
            '/patterns-recommend "streaming job events to multiple UI consumers"',
            '/patterns-recommend "duplicate delivery repeats side effects" --risk operability',
        ],
        "arguments": {
            "query": "add a new SCM provider without changing rule execution code",
            "language": "python",
            "scope": "backend",
            "limit": 5,
        },
    },
    "patterns-scan": {
        "tool": "patterns_scan",
        "purpose": "Scan a file or directory for pattern-relevant architecture smells.",
        "usage": "/patterns-scan <path> [--min-confidence <0-1>] [--pack <pack>] [--include-docs] [--include-generated]",
        "helpCommand": "/patterns-scan help",
        "options": [
            "--min-confidence <0-1>: hide weak findings below the confidence threshold.",
            "--pack <pack>: choose a smell rule pack; default is all.",
            "--include-docs: include documentation files in the scan.",
            "--include-generated: include generated files.",
        ],
        "examples": [
            "/patterns-scan backend/app/workflow_engine --min-confidence 0.45",
            "/patterns-scan backend/app/repositories/jobs.py --min-confidence 0.5",
            "/patterns-scan docs/architecture --include-docs --pack integration",
        ],
        "arguments": {"path": "backend/app/workflow_engine", "min_confidence": 0.45},
    },
    "patterns-context": {
        "tool": "patterns_context",
        "purpose": "Build a model-ready context pack with scan findings, recommendations, snippets, and an ADR seed.",
        "usage": '/patterns-context <path> --query "<problem>" [--language <language>] [--scope <scope>]',
        "helpCommand": "/patterns-context help",
        "options": [
            '--query "<problem>": design question or feature context; required.',
            "--language <language>: optional; inferred from codebase and prompt context when omitted.",
            "--scope <scope>: optional; inferred as object-design, integration-design, a catalog domain, or all when omitted.",
        ],
        "examples": [
            '/patterns-context backend/app/providers/ai --query "adding a new AI provider safely"',
            '/patterns-context frontend/src/state --query "managing streaming job state"',
            '/patterns-context services/orders --query "duplicate message handling and replay"',
        ],
        "arguments": {
            "path": "backend/app/providers/ai",
            "query": "adding a new AI provider safely",
            "language": "python",
            "scope": "backend",
        },
    },
    "patterns-simulate": {
        "tool": "patterns_simulate",
        "purpose": "Score likely pattern options against the architecture decision scorecard.",
        "usage": '/patterns-simulate "<decision or competing options>" [--language <language>] [--risk <risk>] [--limit <n>]',
        "helpCommand": "/patterns-simulate help",
        "options": [
            "--language <language>: optional; inferred from codebase and prompt context when omitted.",
            "--scope is inferred for result context even though this command scores options across the matched catalog set.",
            "--risk <risk>: scorecard emphasis such as operability, simplicity, or balanced.",
            "--limit <n>: number of options to score.",
        ],
        "examples": [
            '/patterns-simulate "Strategy vs Chain of Responsibility for AI provider failover" --risk operability',
            '/patterns-simulate "Command vs State for workflow node execution lifecycle"',
            '/patterns-simulate "event fanout with replay and dead-letter handling" --limit 4',
        ],
        "arguments": {
            "query": "Strategy vs Chain of Responsibility for AI provider failover",
            "language": "python",
            "risk": "operability",
        },
    },
    "patterns-migrate": {
        "tool": "patterns_migrate",
        "purpose": "Create a staged migration plan from a current smell or source shape to a target pattern.",
        "usage": '/patterns-migrate "<current smell or source shape>" --to <target-pattern> [--language <language>] [--query "<context>"]',
        "helpCommand": "/patterns-migrate help",
        "options": [
            "--to <target-pattern>: target pattern slug or name; required.",
            "--language <language>: optional; inferred from codebase and prompt context when omitted.",
            "--scope is inferred for result context even though migration is driven by source and target.",
            '--query "<context>": extra project context.',
        ],
        "examples": [
            '/patterns-migrate "hardcoded if/elif provider selection" --to strategy',
            '/patterns-migrate "fat router with inline persistence and branching" --to facade',
            '/patterns-migrate provider-switch-sprawl --to bridge --query "providers are GitHub, GitLab, and Bitbucket"',
        ],
        "arguments": {
            "source": "hardcoded if/elif provider selection",
            "target": "strategy",
            "language": "python",
        },
    },
    "patterns-snippets": {
        "tool": "patterns_snippets",
        "purpose": "Return language-specific implementation snippets for catalog pattern slugs.",
        "usage": "/patterns-snippets <pattern-slug>[,<pattern-slug>...] [--language <language>]",
        "helpCommand": "/patterns-snippets help",
        "options": [
            "--language <language>: optional; inferred from codebase and prompt context when omitted.",
            "--scope is inferred for result context even though snippet lookup is pattern-slug driven.",
        ],
        "examples": [
            "/patterns-snippets strategy,idempotent-receiver",
            "/patterns-snippets strategy",
            "/patterns-snippets content-based-router,dead-letter-channel",
        ],
        "arguments": {"patterns": ["strategy", "idempotent-receiver"], "language": "python"},
    },
    "patterns-adr": {
        "tool": "patterns_adr",
        "purpose": "Generate an ADR-style decision seed backed by the pattern catalog.",
        "usage": '/patterns-adr "<architecture decision>" [--language <language>] [--scope <scope>] [--status <status>]',
        "helpCommand": "/patterns-adr help",
        "options": [
            "--language <language>: optional; inferred from codebase and prompt context when omitted.",
            "--scope <scope>: optional; inferred as object-design, integration-design, a catalog domain, or all when omitted.",
            "--status <status>: ADR status, default Proposed.",
        ],
        "examples": [
            '/patterns-adr "durable event storage for SSE replay: Redis vs PostgreSQL"',
            '/patterns-adr "choosing between Registry and Chain of Responsibility for executor dispatch"',
            '/patterns-adr "message replay and dead-letter handling for order events"',
        ],
        "arguments": {
            "query": "durable event storage for SSE replay: Redis vs PostgreSQL",
            "language": "python",
            "scope": "backend",
        },
    },
    "patterns-graph": {
        "tool": "patterns_graph",
        "purpose": "Query the typed catalog graph and relationship map.",
        "usage": '/patterns-graph ["relationship question"] [--format json]',
        "helpCommand": "/patterns-graph help",
        "options": [
            "--format json: ask for graph-shaped output when machine-readable relationships are useful.",
            "--language and --scope are not needed; graph queries use the full catalog relationship map.",
        ],
        "examples": [
            '/patterns-graph "what patterns mitigate naive exactly once"',
            "/patterns-graph",
            '/patterns-graph "what patterns are related to observer"',
            '/patterns-graph "which patterns are companions of content-based-router" --format json',
        ],
        "arguments": {"query": "what patterns mitigate naive exactly once"},
    },
    "patterns-examples": {
        "tool": "patterns_examples",
        "purpose": "Show copyable /patterns-* request examples and their backing MCP tool arguments.",
        "usage": "/patterns-examples [topic]",
        "helpCommand": "/patterns-examples help",
        "options": [
            "topic: optional focus area such as scan, context, migrate, adr, graph, snippets, or recommend.",
            "Examples intentionally omit language and scope when inference should choose them from codebase and context.",
        ],
        "examples": [
            "/patterns-examples",
            "/patterns-examples scan",
            "/patterns-examples migration",
        ],
        "arguments": {"topic": "all"},
    },
    "patterns-help": {
        "tool": "patterns_help",
        "purpose": "Show help for all design-pattern slash commands or one command.",
        "usage": "/patterns-help [command]",
        "helpCommand": "/patterns-help help",
        "options": [
            "command: optional command name such as patterns-scan, /patterns-scan, or scan.",
            "Help explains when language and scope are inferred instead of supplied.",
        ],
        "examples": [
            "/patterns-help",
            "/patterns-help patterns-scan",
            "/patterns-help recommend",
        ],
        "arguments": {},
    },
}

SLASH_COMMAND_EXAMPLES: list[dict[str, Any]] = [
    {
        "command": entry["examples"][0],
        "helpCommand": entry["helpCommand"],
        "tool": entry["tool"],
        "arguments": entry["arguments"],
    }
    for name, entry in SLASH_COMMAND_HELP.items()
]


def help_payload(command: str = "") -> dict[str, Any]:
    normalized = command.strip().lower().removeprefix("/").replace("_", "-")
    for suffix in (" help", " --help", " -h"):
        if normalized.endswith(suffix):
            normalized = normalized[: -len(suffix)].strip()
    if normalized and not normalized.startswith("patterns-"):
        normalized = f"patterns-{normalized}"
    if normalized:
        entry = SLASH_COMMAND_HELP.get(normalized)
        return {
            "command": normalized,
            "found": bool(entry),
            "help": entry,
            "availableCommands": sorted(SLASH_COMMAND_HELP),
        }
    return {
        "usage": "Run /<command> help for command-specific help, for example /patterns-scan help.",
        "commands": SLASH_COMMAND_HELP,
    }


def tool_definitions() -> list[dict[str, Any]]:
    string_schema = {"type": "string"}
    return [
        {
            "name": "patterns_recommend",
            "description": 'Recommend catalog patterns, playbooks, recipes, and smells for an architecture force. User slash command: /patterns-recommend "<query>" [--limit 5]. Language and scope are inferred when omitted.',
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
            "description": 'Generate an ADR-style catalog-backed architecture decision seed. User slash command: /patterns-adr "<decision>". Language and scope are inferred when omitted.',
            "inputSchema": {
                "type": "object",
                "properties": {"query": string_schema, "language": string_schema, "scope": string_schema, "status": string_schema},
                "required": ["query"],
            },
        },
        {
            "name": "patterns_context",
            "description": 'Build a model-ready context pack with scan findings, recommendations, snippets, and ADR seed. User slash command: /patterns-context <path> --query "<problem>". Language and scope are inferred when omitted.',
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
            "description": 'Score likely pattern options against the architecture decision scorecard. User slash command: /patterns-simulate "<decision>" [--risk operability]. Language and scope context are inferred when omitted.',
            "inputSchema": {
                "type": "object",
                "properties": {"query": string_schema, "language": string_schema, "risk": string_schema, "limit": {"type": "integer"}},
                "required": ["query"],
            },
        },
        {
            "name": "patterns_migrate",
            "description": 'Create a recipe-backed migration plan from a smell/current shape to a target pattern. User slash command: /patterns-migrate "<current smell>" --to <target-pattern>. Language and scope context are inferred when omitted.',
            "inputSchema": {
                "type": "object",
                "properties": {"source": string_schema, "target": string_schema, "language": string_schema, "query": string_schema},
                "required": ["source", "target"],
            },
        },
        {
            "name": "patterns_snippets",
            "description": "Return language-specific implementation snippets for catalog pattern slugs. User slash command: /patterns-snippets strategy,idempotent-receiver. Language and scope context are inferred when omitted.",
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
        {
            "name": "patterns_help",
            "description": "Return help for all /patterns-* commands or one command. Use when a user asks what a design-pattern command does, including /<command> help.",
            "inputSchema": {
                "type": "object",
                "properties": {"command": string_schema},
            },
        },
    ]


def _json_text(value: Any) -> dict[str, str]:
    return {"type": "text", "text": json.dumps(value, indent=2, sort_keys=True)}


def _inference(
    arguments: dict[str, Any],
    *,
    query: str = "",
    paths: list[str] | None = None,
) -> dict[str, Any]:
    language = arguments.get("language")
    scope = arguments.get("scope")
    return infer_request_context(
        query=query,
        paths=paths or [],
        language=str(language).strip() if language else None,
        scope=str(scope).strip() if scope else None,
    )


def _add_inference(payload: Any, inference: dict[str, Any]) -> Any:
    if isinstance(payload, dict):
        enriched = dict(payload)
        enriched["inference"] = inference
        return enriched
    return payload


def call_tool(name: str, arguments: dict[str, Any]) -> Any:
    if name == "patterns_help":
        return help_payload(str(arguments.get("command", "")))
    if name == "patterns_examples":
        topic = str(arguments.get("topic", "")).strip()
        return {
            "usage": "When users ask for example MCP requests, lead with these copyable slash commands instead of describing tool schemas.",
            "format": '/patterns-<action> <required-argument> [--optional-flag value]',
            "topic": topic or "all",
            "slashCommands": SLASH_COMMAND_EXAMPLES,
            "help": "Run /<command> help for command-specific help, for example /patterns-recommend help.",
        }
    if name == "patterns_recommend":
        query = str(arguments.get("query", ""))
        inference = _inference(arguments, query=query)
        return recommend_entries(
            query,
            scope=str(inference.get("scope") or "all"),
            language=inference.get("language") or None,
            risk=str(arguments.get("risk", "balanced")),
            limit=int(arguments.get("limit", 8)),
            include_snippets=True,
        )
    if name == "patterns_scan":
        path = str(arguments.get("path", "."))
        inference = _inference(arguments, query=path, paths=[path])
        return _add_inference(
            scan_path(
                path,
                pack=str(arguments.get("pack", "all")),
                include_docs=bool(arguments.get("include_docs", False)),
                include_generated=bool(arguments.get("include_generated", False)),
                min_confidence=float(arguments.get("min_confidence", 0.0)),
            ),
            inference,
        )
    if name == "patterns_adr":
        query = str(arguments.get("query", ""))
        inference = _inference(arguments, query=query)
        return _add_inference(
            adr_payload(
                query,
                status=str(arguments.get("status", "Proposed")),
                language=inference.get("language") or None,
                scope=str(inference.get("scope") or "all"),
            ),
            inference,
        )
    if name == "patterns_context":
        path = str(arguments.get("path", "."))
        query = str(arguments.get("query", ""))
        inference = _inference(arguments, query=query, paths=[path])
        return _add_inference(
            context_pack(
                path,
                query,
                language=inference.get("language") or None,
                scope=str(inference.get("scope") or "all"),
            ),
            inference,
        )
    if name == "patterns_graph":
        query = str(arguments.get("query", "")).strip()
        return graph_query(query) if query else catalog_graph()
    if name == "patterns_simulate":
        query = str(arguments.get("query", ""))
        inference = _inference(arguments, query=query)
        return _add_inference(
            decision_simulation(
                query,
                language=inference.get("language") or None,
                risk=str(arguments.get("risk", "balanced")),
                limit=int(arguments.get("limit", 5)),
            ),
            inference,
        )
    if name == "patterns_migrate":
        query = " ".join(
            part
            for part in [
                str(arguments.get("source", "")),
                str(arguments.get("target", "")),
                str(arguments.get("query", "")),
            ]
            if part
        )
        inference = _inference(arguments, query=query)
        return _add_inference(
            migration_plan(
                str(arguments.get("source", "")),
                str(arguments.get("target", "")),
                language=inference.get("language") or None,
                query=str(arguments.get("query", "")),
            ),
            inference,
        )
    if name == "patterns_snippets":
        patterns = set(arguments.get("patterns", []))
        inference = _inference(arguments, query=" ".join(sorted(patterns)))
        return snippet_matches(patterns, inference.get("language") or None)
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
