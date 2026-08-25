import json
import os
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

    def test_publish_workflow_uses_immutable_validated_candidate(self):
        workflow_path = ROOT / ".github" / "workflows" / "publish.yml"
        self.assertTrue(workflow_path.is_file())
        workflow = load_json(workflow_path)
        self.assertEqual(workflow["on"], {"push": {"tags": ["v*"]}})
        self.assertEqual(workflow["permissions"], {})
        self.assertEqual(set(workflow["jobs"]), {"validate", "publish"})
        validate = workflow["jobs"]["validate"]
        self.assertEqual(validate["permissions"], {"contents": "read"})
        self.assertEqual(set(validate["outputs"]), {"version", "release_root"})
        commands = "\n".join(step.get("run", "") for step in validate["steps"])
        self.assertIn("python3 scripts/release_inventory.py", commands)
        self.assertIn("python3 scripts/build_release.py", commands)
        self.assertIn("python3 scripts/validate_catalog.py", commands)
        self.assertIn("python3 plugins/design-patterns/scripts/validate_catalog.py", commands)
        self.assertIn("python3 -m unittest tests.test_release_contract", commands)
        self.assertIn('"$RUNNER_TEMP/bytedesk-publisher/bdm" validate bytedesk-package.yaml', commands)
        setup = next(step for step in validate["steps"] if step.get("name") == "Install the immutable audited publisher")
        self.assertEqual(
            setup["uses"],
            "ByteDeskAI/marketplace-publisher/.github/actions/setup-bdm@7cf1e847d6383c32dc9b125c19e9b4d8f4212e41",
        )
        self.assertEqual(setup["with"]["expected-sha256"], "789f84da539fe2cd0e9b1d09db56fe8e7c2a6061ee0d71484ee72c7094b254c1")
        upload = next(step for step in validate["steps"] if str(step.get("uses", "")).startswith("actions/upload-artifact@"))
        self.assertEqual(upload["uses"], "actions/upload-artifact@ea165f8d65b6e75b540449e92b4886f43607fa02")
        self.assertEqual(upload["with"]["name"], "bdm-publication-source")
        self.assertEqual(upload["with"]["path"], "bytedesk-package.yaml\ndist/design-patterns\n")
        self.assertIs(upload["with"]["include-hidden-files"], True)
        self.assertEqual(upload["with"]["retention-days"], 1)

        publish = workflow["jobs"]["publish"]
        self.assertEqual(publish["needs"], "validate")
        self.assertEqual(publish["permissions"], {"actions": "read", "contents": "read", "id-token": "write"})
        self.assertEqual(
            publish["uses"],
            "ByteDeskAI/marketplace-publisher/.github/workflows/publish-v1.yml@f6abdb916e21112eb3ccfc1af03b8043498c3a50",
        )
        self.assertEqual(publish["with"], {
            "package": "@bytedesk/design-patterns",
            "version": "${{ needs.validate.outputs.version }}",
            "source-commit": "${{ github.sha }}",
            "release-root": "${{ needs.validate.outputs.release_root }}",
        })
        raw = workflow_path.read_text(encoding="utf-8")
        for forbidden in [
            "secrets.",
            "bdm publish",
            "bdm login",
            "go install",
            "curl ",
            "ACTIONS_ID_TOKEN_REQUEST",
            "workflow_dispatch",
            '"release":',
            "exit 1",
        ]:
            self.assertNotIn(forbidden, raw)

    def test_publish_validation_output_parser_binds_tag_package_and_root(self):
        workflow = load_json(ROOT / ".github" / "workflows" / "publish.yml")
        release = next(step for step in workflow["jobs"]["validate"]["steps"] if step.get("id") == "release")
        validator = release["run"].split("python3 - <<'PY'\n", 1)[1].rsplit("\nPY\n", 1)[0]
        payload = {
            "schemaVersion": 1,
            "package": "@bytedesk/design-patterns",
            "version": VERSION,
            "manifestDigest": "sha256:" + "b" * 64,
            "releaseRootDigest": "sha256:" + "a" * 64,
            "validatorRevision": "providers-v1",
            "variants": [{"id": "claude-code"}],
        }
        with tempfile.TemporaryDirectory() as temporary:
            root = Path(temporary)
            result_path = root / "validation.json"
            output_path = root / "github-output"
            result_path.write_text(json.dumps(payload, separators=(",", ":")) + "\n", encoding="utf-8")
            environment = os.environ.copy()
            environment.update(
                RESULT_PATH=str(result_path), GITHUB_OUTPUT=str(output_path),
                GITHUB_REF_NAME="v" + VERSION, EXPECTED_PACKAGE="@bytedesk/design-patterns",
            )
            result = subprocess.run(["python3", "-c", validator], env=environment, text=True, capture_output=True)
            self.assertEqual(result.returncode, 0, result.stderr)
            self.assertEqual(
                output_path.read_text(encoding="utf-8"),
                f"version={VERSION}\nrelease_root=sha256:{'a' * 64}\n",
            )
            payload["releaseRootDigest"] = "not-a-digest"
            result_path.write_text(json.dumps(payload) + "\n", encoding="utf-8")
            rejected = subprocess.run(["python3", "-c", validator], env=environment, text=True, capture_output=True)
            self.assertNotEqual(rejected.returncode, 0)
            self.assertIn("release root is invalid", rejected.stderr)

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
