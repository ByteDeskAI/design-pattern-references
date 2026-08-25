import json
import subprocess
import tempfile
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
PLUGIN = ROOT / "plugins" / "design-patterns"
VERSION = "0.9.3"


def load_json(path: Path):
    return json.loads(path.read_text(encoding="utf-8"))


class ReleaseContractTests(unittest.TestCase):
    def test_provider_manifests_are_complete_and_versioned_by_policy(self):
        claude = load_json(PLUGIN / ".claude-plugin" / "plugin.json")
        claude_marketplace = load_json(ROOT / ".claude-plugin" / "marketplace.json")
        codex = load_json(PLUGIN / ".codex-plugin" / "plugin.json")
        grok = load_json(PLUGIN / ".grok-plugin" / "plugin.json")
        kimi = load_json(PLUGIN / "kimi.plugin.json")

        self.assertNotIn("version", claude)
        self.assertNotIn("version", claude_marketplace)
        self.assertNotIn("version", claude_marketplace["plugins"][0])
        self.assertEqual(codex["version"], VERSION)
        self.assertEqual(grok["version"], VERSION)
        self.assertEqual(kimi["version"], VERSION)
        self.assertEqual({claude["name"], codex["name"], grok["name"], kimi["name"]}, {"design-patterns"})

    def test_bytedesk_release_declares_exact_four_provider_contracts(self):
        release = load_json(ROOT / "bytedesk-package.yaml")
        self.assertEqual(release["metadata"]["namespace"], "bytedesk")
        self.assertEqual(release["metadata"]["name"], "design-patterns")
        self.assertEqual(release["metadata"]["version"], VERSION)
        variants = release["spec"]["variants"]
        self.assertEqual(
            [(item["id"], item["provider"], item["contract"], item["contractVersion"]) for item in variants],
            [
                ("claude-code", "claude-code", "claude-plugin", "observed-2026-08-19"),
                ("openai-codex", "openai-codex", "codex-plugin", "observed-2026-08-19"),
                ("grok-build", "grok-build", "grok-plugin", "main-observed-2026-08-19"),
                ("kimi-code", "kimi-code", "kimi-plugin", "0.38.0"),
            ],
        )
        self.assertEqual({item["source"]["path"] for item in variants}, {"dist/design-patterns"})

    def test_release_tree_is_self_contained_and_portable(self):
        self.assertEqual((ROOT / "LICENSE").read_bytes(), (PLUGIN / "LICENSE").read_bytes())
        self.assertEqual((ROOT / "NOTICE").read_bytes(), (PLUGIN / "NOTICE").read_bytes())
        self.assertFalse([path for path in PLUGIN.rglob("*") if path.is_symlink()])
        for relative in ["skills", "agents", "commands", ".mcp.json", ".portable-mcp.json"]:
            self.assertTrue((PLUGIN / relative).exists(), relative)
        for readme in [ROOT / "README.md", PLUGIN / "README.md"]:
            text = readme.read_text(encoding="utf-8")
            self.assertNotIn("/" + "Users/", text)
            self.assertNotIn("ByteDeskAI/" + "bytedesk-marketplace", text)

    def test_codex_mcp_uses_artifact_relative_command_without_root_cwd(self):
        manifest = load_json(PLUGIN / ".codex-mcp.json")
        server = manifest["mcpServers"]["design-patterns"]
        self.assertEqual(server["command"], "./bin/patterns-mcp")
        # The server contract accepts cwd only when it names a concrete
        # directory represented by files in the artifact. The artifact root
        # is already the runtime base, so declaring cwd "." is both redundant
        # and invalid under codex-plugin-v1 validation.
        self.assertNotIn("cwd", server)

    def test_publish_workflow_is_oidc_only_and_fails_closed_after_candidate_upload(self):
        workflow_path = ROOT / ".github" / "workflows" / "publish.yml"
        self.assertTrue(workflow_path.is_file())
        workflow = load_json(workflow_path)
        self.assertEqual(workflow["permissions"], {"contents": "read", "id-token": "write"})
        publish = workflow["jobs"]["publish"]
        self.assertEqual(publish["environment"], "marketplace-production")
        commands = "\n".join(step.get("run", "") for step in publish["steps"])
        self.assertIn("python3 scripts/release_inventory.py", commands)
        self.assertIn("python3 scripts/build_release.py", commands)
        self.assertIn("python3 scripts/validate_catalog.py", commands)
        self.assertIn("python3 plugins/design-patterns/scripts/validate_catalog.py", commands)
        self.assertIn("python3 -m unittest tests.test_release_contract", commands)
        self.assertIn("exit 1", commands)
        upload = next(step for step in publish["steps"] if step.get("uses") == "actions/upload-artifact@v4")
        self.assertEqual(upload["with"]["name"], "design-patterns-release-candidate")
        self.assertIn("bytedesk-package.yaml", upload["with"]["path"])
        self.assertIn("dist/design-patterns", upload["with"]["path"])
        self.assertIn("dist/release-inventory.json", upload["with"]["path"])
        raw = workflow_path.read_text(encoding="utf-8")
        for forbidden in [
            "secrets.",
            "bdm publish",
            "bdm login",
            "go install",
            "curl ",
            "ACTIONS_ID_TOKEN_REQUEST",
        ]:
            self.assertNotIn(forbidden, raw)

    def test_source_tree_recipe_has_a_stable_inventory(self):
        recipe = load_json(ROOT / "packaging" / "source-tree-v1.json")
        self.assertEqual(recipe["id"], "source-tree-v1")
        self.assertEqual(recipe["source"], "plugins/design-patterns")
        self.assertEqual(recipe["output"], "dist/design-patterns")
        self.assertEqual(recipe["variants"], ["claude-code", "openai-codex", "grok-build", "kimi-code"])
        command = ["python3", str(ROOT / "scripts" / "release_inventory.py")]
        first = subprocess.run(command, check=True, capture_output=True, text=True).stdout
        second = subprocess.run(command, check=True, capture_output=True, text=True).stdout
        self.assertEqual(first, second)
        inventory = json.loads(first)
        self.assertTrue(inventory["inventoryDigest"].startswith("sha256:"))
        paths = {item["path"] for item in inventory["files"]}
        self.assertIn(".claude-plugin/plugin.json", paths)
        self.assertIn(".codex-plugin/plugin.json", paths)
        self.assertIn(".grok-plugin/plugin.json", paths)
        self.assertIn("kimi.plugin.json", paths)

    def test_release_staging_excludes_runtime_caches_and_preserves_inventory(self):
        with tempfile.TemporaryDirectory() as temporary:
            output = Path(temporary) / "design-patterns"
            subprocess.run(
                ["python3", str(ROOT / "scripts" / "build_release.py"), "--output", str(output)],
                check=True,
                capture_output=True,
                text=True,
            )
            self.assertFalse(list(output.rglob("__pycache__")))
            self.assertFalse(list(output.rglob("*.pyc")))
            staged = {
                path.relative_to(output).as_posix(): (path.read_bytes(), path.stat().st_mode & 0o777)
                for path in output.rglob("*")
                if path.is_file()
            }
            source_inventory = json.loads(
                subprocess.run(
                    ["python3", str(ROOT / "scripts" / "release_inventory.py")],
                    check=True,
                    capture_output=True,
                    text=True,
                ).stdout
            )
            self.assertEqual(set(staged), {item["path"] for item in source_inventory["files"]})
            for item in source_inventory["files"]:
                self.assertEqual(staged[item["path"]][1], int(item["mode"], 8))


if __name__ == "__main__":
    unittest.main()
