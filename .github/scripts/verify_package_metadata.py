#!/usr/bin/env python3
"""Reads pyproject.toml once and checks the two invariants the release
pipeline (jh-client-generator's write-package-metadata.mjs) is supposed to
have already guaranteed before tagging: the version matches the tag exactly,
and a Source API Version was recorded. A mismatch here means something
upstream broke, and publishing on top of that would ship a lie. Mirrors
jsonhub-sdk-ts's verify-package-metadata.cjs.
"""

import os
import sys
import tomllib

tag = os.environ.get("GITHUB_REF_NAME")
if not tag:
    print("GITHUB_REF_NAME is not set.", file=sys.stderr)
    sys.exit(1)

with open("pyproject.toml", "rb") as f:
    manifest = tomllib.load(f)

poetry = manifest.get("tool", {}).get("poetry", {})
jsonhub = manifest.get("tool", {}).get("jsonhub", {})

version = poetry.get("version")
tag_version = tag.removeprefix("v")
if tag_version != version:
    print(f"Tag {tag} does not match pyproject.toml version {version}.", file=sys.stderr)
    sys.exit(1)

source_api_version = jsonhub.get("source_api_version")
if not isinstance(source_api_version, str) or not source_api_version.strip():
    print("pyproject.toml is missing a non-empty [tool.jsonhub].source_api_version.", file=sys.stderr)
    sys.exit(1)

print(f'pyproject.toml version {version} matches tag {tag}; source_api_version is "{source_api_version}".')
