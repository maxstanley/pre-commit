from __future__ import annotations

import importlib.metadata

CONFIG_FILE = '.pre-commit-config.yaml'
CONFIG_FILE_SEARCH = ['.config/pre-commit/', f".config/{CONFIG_FILE}", CONFIG_FILE]
MANIFEST_FILE = '.pre-commit-hooks.yaml'

# Bump when modifying `empty_template`
LOCAL_REPO_VERSION = '1'

VERSION = importlib.metadata.version('pre_commit')

DEFAULT = 'default'
