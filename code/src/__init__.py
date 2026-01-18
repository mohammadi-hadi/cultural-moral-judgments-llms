"""
Analysis code for cultural moral judgments with LLMs.

This module provides utilities for:
- Data processing (WVS and PEW survey data)
- Visualization of model evaluation results
- Configuration and logging utilities
"""

from .data_processing import (
    COUNTRIES_PEW_ALL,
    COUNTRIES_WVS_W7_ALL,
    PEW_QUESTIONS_TEXT,
    W7_QUESTIONS_TEXT,
    get_all_countries,
    get_pew_ratings,
    get_question_mapping,
    get_wvs_ratings,
    load_pew_data,
    load_wvs_data,
)
from .utils import (
    ensure_directories,
    format_time,
    get_available_models,
    get_model_short_name,
    load_config,
    save_results,
    setup_logging,
)
from .visualization import (
    create_summary_report,
    plot_correlation_scatter,
    plot_country_performance,
    plot_model_comparison,
    plot_topic_heatmap,
)

__version__ = "1.0.0"
__all__ = [
    # Data processing
    "load_wvs_data",
    "load_pew_data",
    "get_wvs_ratings",
    "get_pew_ratings",
    "get_question_mapping",
    "get_all_countries",
    "COUNTRIES_WVS_W7_ALL",
    "COUNTRIES_PEW_ALL",
    "W7_QUESTIONS_TEXT",
    "PEW_QUESTIONS_TEXT",
    # Visualization
    "plot_correlation_scatter",
    "plot_model_comparison",
    "plot_topic_heatmap",
    "plot_country_performance",
    "create_summary_report",
    # Utils
    "setup_logging",
    "load_config",
    "save_results",
    "get_model_short_name",
    "ensure_directories",
    "get_available_models",
    "format_time",
]
