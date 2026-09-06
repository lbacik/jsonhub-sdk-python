#!/usr/bin/env python3
"""Exercises the built package the way a real consumer would, gating
publication on it: builds it with `poetry build`, installs the wheel into a
scratch virtualenv, and imports it from there. A broken SDK Release can't be
unpublished cleanly, so this is the check that stands between a build mistake
(a missing module, a broken dependency pin) and the registry. Mirrors
jsonhub-sdk-ts's smoke-test.cjs.

The assertions stay generic across every future SDK Surface (new operations,
new models): every openapi-python-client output exposes a Client and an
AuthenticatedClient from its top-level package - this never checks a specific
operation or model name, since those change with the API itself.
"""

import shutil
import subprocess
import sys
import tempfile
import tomllib
import venv
from pathlib import Path

repo_root = Path(__file__).resolve().parents[2]

with open(repo_root / "pyproject.toml", "rb") as f:
    manifest = tomllib.load(f)

poetry = manifest["tool"]["poetry"]
package_name = poetry["name"]
package_import_name = poetry["packages"][0]["include"]

print(f"Building {package_name}@{poetry['version']}...")
dist_dir = repo_root / "dist"
shutil.rmtree(dist_dir, ignore_errors=True)
subprocess.run(["poetry", "build", "-f", "wheel"], cwd=repo_root, check=True)

wheels = list(dist_dir.glob("*.whl"))
if len(wheels) != 1:
    raise RuntimeError(f"Expected exactly one built wheel, found {len(wheels)}: {wheels}")
wheel_path = wheels[0]

venv_dir = Path(tempfile.mkdtemp(prefix="jsonhub-sdk-python-smoke-"))
try:
    print(f"Installing the built wheel into a fresh virtualenv at {venv_dir}...")
    venv.create(venv_dir, with_pip=True)
    venv_python = venv_dir / "bin" / "python"
    subprocess.run([str(venv_python), "-m", "pip", "install", "--quiet", str(wheel_path)], check=True)

    check_script = f"""
import {package_import_name} as mod

for name in ("Client", "AuthenticatedClient"):
    if not hasattr(mod, name):
        raise AssertionError(f"Expected the package to export {{name}}.")
    cls = getattr(mod, name)
    if not isinstance(cls, type):
        raise AssertionError(f"Expected {{name}} to be a class.")

client = mod.Client(base_url="https://example.invalid")
authenticated_client = mod.AuthenticatedClient(base_url="https://example.invalid", token="smoke-test-token")

print(f"Smoke test passed: {{mod.__name__}} exports Client and AuthenticatedClient, both instantiate correctly.")
"""
    subprocess.run([str(venv_python), "-c", check_script], check=True)
finally:
    shutil.rmtree(venv_dir, ignore_errors=True)
