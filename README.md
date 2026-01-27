<div align="center">

# Cultural Moral Judgments in LLMs

### Exploring Cultural Variations in Moral Judgments with Large Language Models

[![ECAI 2025](https://img.shields.io/badge/ECAI-2025-orange.svg)](https://ecai2025.eu/)
[![arXiv](https://img.shields.io/badge/arXiv-2506.12433-b31b1b.svg)](https://arxiv.org/abs/2506.12433)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)
[![Python 3.8+](https://img.shields.io/badge/python-3.8+-blue.svg)](https://www.python.org/downloads/)

*Exploring how LLMs represent and align with cultural variations in moral judgments across 55+ countries*

[Paper](https://arxiv.org/abs/2506.12433) • [Code](https://github.com/mohammadi-hadi/cultural-moral-judgments-llms-code) • [Website](https://mohammadi.cv)

---

</div>

## Paper

**Title:** Exploring Cultural Variations in Moral Judgments with Large Language Models

**Authors:** Hadi Mohammadi, Ayoub Bagheri

**Affiliation:** Utrecht University, The Netherlands

**arXiv:** [2506.12433](https://arxiv.org/abs/2506.12433)

## Overview

We investigate whether LLMs can capture the nuanced moral reasoning patterns that vary across cultures and contexts, using data from the World Values Survey (WVS) spanning 55+ countries.

<div align="center">
<img src="CLIN_submission/figures/country_heatmap_WVS.png" alt="Country-wise Moral Alignment" width="800"/>
<br><i>Country-wise correlation between LLM predictions and human moral judgments</i>
</div>

## Key Findings

- Large language models show significant alignment with human moral judgments (r > 0.85 for top-tier models)
- Performance varies substantially across cultural contexts
- Western-centric training data leads to better alignment with Western moral norms
- Larger models generally show better cross-cultural alignment

<div align="center">
<img src="CLIN_submission/figures/model_pairwise_correlation_WVS.png" alt="Model Pairwise Correlation" width="600"/>
<br><i>Pairwise correlation between LLM predictions across models</i>
</div>

## Quick Start

```bash
# Clone the repository
git clone https://github.com/mohammadi-hadi/cultural-moral-judgments-llms.git
cd cultural-moral-judgments-llms

# Install dependencies
pip install -r code/requirements.txt

# Generate plots
cd code
python scripts/generate_plots.py --results-dir ../results --output-dir ../figures
```

## Repository Structure

```
cultural-moral-judgments-llms/
├── CLIN_submission/                    # CLIN Journal submission
│   ├── main.pdf                        # Full paper
│   ├── main.tex                        # LaTeX source
│   ├── figures/                        # Paper figures
│   └── references.bib                  # Bibliography
├── CLINJ_template__Copy_/              # CLIN Journal template
├── Project05_LNCS_Springer_Submission/ # LNCS/Springer submission
├── code/                               # Analysis code
│   ├── src/                            # Source modules
│   │   ├── __init__.py                 # Package initialization
│   │   ├── data_processing.py          # WVS/PEW data loading
│   │   ├── visualization.py            # Plotting utilities
│   │   └── utils.py                    # Helper functions
│   ├── scripts/                        # Analysis scripts
│   │   └── generate_plots.py           # Plot generation script
│   └── requirements.txt                # Python dependencies
└── README.md
```

## Installation

```bash
git clone https://github.com/mohammadi-hadi/cultural-moral-judgments-llms.git
cd cultural-moral-judgments-llms
pip install -r code/requirements.txt
```

## Usage

### Loading Survey Data

```python
from code.src import load_wvs_data, load_pew_data, get_question_mapping

# Load WVS moral judgment data
wvs_df = load_wvs_data("path/to/wvs_data.csv")

# Get question text mapping
questions = get_question_mapping("wvs")
print(questions)
```

### Generating Plots

```bash
cd code
python scripts/generate_plots.py --results-dir ../results --output-dir ../figures
```

## Methodology

1. **Data Collection**: World Values Survey moral judgment questions from 55+ countries
2. **Model Evaluation**: Test 17 LLMs (GPT, Claude, LLaMA, Falcon, etc.)
3. **Scoring Methods**: Log-probability and Chain-of-Thought reasoning
4. **Analysis**: Correlation with human responses, cross-cultural comparison

## Citation

```bibtex
@article{mohammadi2025cultural,
  title={Exploring Cultural Variations in Moral Judgments with Large Language Models},
  author={Mohammadi, Hadi and Giachanou, Anastasia and Bagheri, Ayoub},
  journal={arXiv preprint arXiv:2506.12433},
  year={2025}
}
```

## Related Work

This research is part of the PhD thesis "From Tokens to Thoughts: Explainable NLP for Understanding Large Language Models" by Hadi Mohammadi at Utrecht University (2025).

See also: [EvalMORAAL](https://github.com/mohammadi-hadi/EvalMORAAL) - Our comprehensive LLM moral evaluation framework.

## License

This work is licensed under the MIT License.

## Contact

- Hadi Mohammadi - [h.mohammadi@uu.nl](mailto:h.mohammadi@uu.nl)
- Website: [mohammadi.cv](https://mohammadi.cv)
