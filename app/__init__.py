"""
Top-level package exports for `app`.

This file collects commonly used submodules and helpers so callers can import
from `app` directly, e.g. `from app import get_logger, text_processing`.
"""

# Core utilities
from .utils import (
	get_logger,
	get_env,
	ensure_dir,
	compute_text_hash,
	load_json,
	save_json,
)

# Subpackages (re-exported modules for convenience)
from . import checker
from . import storage
from . import text_processing
from . import perfomance_tests
from . import search_export

__all__ = [
	# utils
	"get_logger",
	"get_env",
	"ensure_dir",
	"compute_text_hash",
	"load_json",
	"save_json",

	# subpackages
	"checker",
	"storage",
	"text_processing",
	"perfomance_tests",
	"search_export",
]

