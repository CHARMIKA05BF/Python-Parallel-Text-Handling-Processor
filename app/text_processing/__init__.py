from .text_breaker import clean_text, break_text_into_groups
from .text_loader import load_file, load_all_texts

# Two pipeline implementations are provided — one simple and one with
# deduplication and hashing. Import both with explicit names to avoid
# collision when imported from the package root.
from .parallel_break_loader import (
	parallel_process_text as parallel_process_text_simple,
	pipeline_from_folder as pipeline_from_folder_simple,
)

from .parallel_break_loader import (
	parallel_process_text as parallel_process_text_dedup,
	pipeline_from_folder as pipeline_from_folder_dedup,
)

__all__ = [
	"clean_text",
	"break_text_into_groups",
	"load_file",
	"load_all_texts",
	"parallel_process_text_simple",
	"parallel_process_text_dedup",
	"pipeline_from_folder_simple",
	"pipeline_from_folder_dedup",
]

