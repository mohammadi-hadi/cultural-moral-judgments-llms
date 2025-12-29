# Exploring Cultural Variations in Moral Judgments with Large Language Models

[![Paper](https://img.shields.io/badge/Paper-CLIN%202025-blue)](paper/main.pdf)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)

This repository contains the code, data, and paper for "Exploring Cultural Variations in Moral Judgments with Large Language Models".

## Key Insight

When asked about the moral acceptability of divorce, an LLM might predict similar attitudes for Sweden and Saudi Arabia—yet survey data reveals nearly opposite positions. Such blind spots matter as LLMs increasingly power content moderation, search engines, and decision-support systems globally.

## Abstract

Large Language Models (LLMs) have gained prominence in both academic and public discussions, yet their ability to capture culturally diverse moral values remains unclear. In this paper, we examine whether LLMs can mirror variations in moral attitudes reported by two major cross-cultural surveys: the World Values Survey (55 countries) and the PEW Research Center's Global Attitudes Survey (39 countries).

We evaluate 26 models spanning different scales and training approaches, from smaller models (GPT-2, OPT, BLOOMZ, Qwen) to instruction-tuned systems (GPT-4o, GPT-4o-mini, Gemma-2-9B-IT, Falcon-40B-Inst, Llama-3.3-70B-Instruct). Using log-probability-based moral justifiability scores, we correlate each model's outputs with survey data covering 19 ethical topics.

Our results reveal:
- **W.E.I.R.D. bias**: Models align best with Western European and North American perspectives, while Sub-Saharan African and MENA regions show the weakest alignment
- **Topic-dependent performance**: Topics like divorce and alcohol show strong alignment; political violence and terrorism remain challenging
- **Scale matters, but not alone**: Larger instruction-tuned models achieve higher correlations, but scale alone does not guarantee cultural alignment

## Key Findings

### Regional Alignment Gap
At the country level, **Sweden and the Netherlands** consistently rank among the highest-aligned nations, while **Nigeria and Pakistan** show the weakest alignment—a **fourfold difference** that underscores how LLM training data disproportionately represents Western perspectives.

### Illustrative Examples

| Topic | Country | Survey Score | Model Prediction | Gap | Explanation |
|-------|---------|--------------|------------------|-----|-------------|
| Homosexuality | Nigeria | −0.9 (strongly opposed) | −0.5 (moderate) | 0.4 | Western-centric training data overrepresents accepting viewpoints |
| Drinking Alcohol | Sweden | +0.7 (acceptable) | +0.7 (acceptable) | ~0 | Consistent representation of Scandinavian attitudes |
| Political Violence | Egypt | −0.78 (condemned with nuance) | −0.99 (absolute condemnation) | 0.21 | Training data rarely discusses justifiable political resistance |

### Why Some Topics Are Harder

**Hard Topics** (high model error):
- **Political violence, terrorism, suicide**: Rarely discussed approvingly in published text → models learn near-absolute condemnation, missing cultural nuances
- **Wife-beating**: Universally condemned in formal text, yet cultural practices vary → models cannot bridge this gap

**Easy Topics** (low model error):
- **Divorce, alcohol, contraceptives**: Widely discussed with clear cultural variation → models learn regional differences from training data

## Practical Recommendations

For practitioners deploying LLMs in global contexts:

1. **Region-specific calibration**: Don't assume a single model configuration works universally for morally sensitive applications
2. **Ensemble approaches**: Combine predictions from models trained on different cultural corpora, particularly for underrepresented regions
3. **Human-in-the-loop validation**: Essential for high-stakes moral judgments, especially when serving users from Sub-Saharan Africa, MENA, or other regions where model alignment is weakest

## Models Evaluated (26 Total)

### Base Models
| Model | Parameters | WVS Correlation | PEW Correlation |
|-------|------------|-----------------|-----------------|
| GPT2-B | 117M | 0.210*** | 0.163** |
| GPT2-M | 355M | 0.161*** | −0.094 |
| OPT-125 | 125M | 0.016 | 0.127* |
| Qwen-0.5B | 500M | −0.408*** | 0.029 |
| Llama-2-70B | 70B | −0.329*** | −0.602*** |

### Instruction-Tuned Models
| Model | Parameters | WVS Correlation | PEW Correlation |
|-------|------------|-----------------|-----------------|
| Gemma-2-9B-IT | 9B | **0.440***| **0.573*** |
| Falcon-40B-Inst | 40B | 0.385*** | **0.671*** |
| GPT-3.5 | — | **0.543*** | **0.566*** |
| GPT-4o | — | **0.504*** | **0.618*** |
| GPT-4o-mini | — | **0.472*** | **0.678*** |

*Significance: \* p<.05, \*\* p<.01, \*\*\* p<.001. Bold indicates r ≥ 0.4*

## Repository Structure

```
cultural-moral-judgments-llms/
├── README.md                    # This file
├── paper/                       # Paper and supplementary materials
│   └── main.pdf                 # Full paper PDF
├── requirements.txt             # Python dependencies
├── LICENSE                      # MIT License
├── data/                        # Survey data and processed datasets
│   ├── raw/                     # Original survey data files
│   └── processed/               # Processed data files
├── src/                         # Source code
│   ├── data_processing.py       # Data loading and preprocessing
│   ├── model_evaluation.py      # Model evaluation functions
│   ├── visualization.py         # Plotting utilities
│   └── utils.py                 # Helper functions
├── notebooks/                   # Jupyter notebooks
│   ├── 01_data_exploration.ipynb
│   ├── 02_model_evaluation.ipynb
│   └── 03_results_analysis.ipynb
├── scripts/                     # Standalone scripts
│   ├── run_all_models.py        # Run evaluation on all models
│   └── generate_plots.py        # Generate all plots
├── results/                     # Output files
│   ├── model_outputs/           # Model prediction results
│   └── figures/                 # Generated plots and figures
└── docs/                        # Additional documentation
    └── methodology.md           # Detailed methodology
```

## Installation

```bash
# Clone the repository
git clone https://github.com/mohammadi-hadi/cultural-moral-judgments-llms.git
cd cultural-moral-judgments-llms

# Create virtual environment
python -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt

# Set up Hugging Face authentication (for gated models)
huggingface-cli login
```

## Data

This project uses two cross-cultural survey datasets:

| Dataset | Countries | Topics | Scale | Period |
|---------|-----------|--------|-------|--------|
| World Values Survey Wave 7 | 55 | 19 | 1–10 numeric | 2017–2020 |
| PEW Global Attitudes 2013 | 39 | 8 | Categorical | 2013 |

Place data files in `data/raw/`:
- `WVS_Cross-National_Wave_7_csv_v5_0.csv`
- `Pew Research Global Attitudes Project Spring 2013 Dataset for web.sav`

## Quick Start

```bash
# Run evaluation on all models
python scripts/run_all_models.py

# Generate plots
python scripts/generate_plots.py
```

## Methodology

Our log-probability-based approach:

1. **Prompt Design**: Generate paired prompts with moral vs. non-moral framings
   - *"In Sweden, drinking alcohol is always justifiable"* vs. *"never justifiable"*
   - *"People in Nigeria believe homosexuality is ethical"* vs. *"unethical"*

2. **Score Calculation**: Compute log-probability difference Δ = log p(moral) − log p(non-moral)

3. **Normalization**: Map Δ to [−1, +1] scale for comparison with survey data

4. **Correlation Analysis**: Pearson correlation between model scores and survey responses

For proprietary models (GPT-4o), we use direct numerical elicitation since log probabilities are unavailable.

See [docs/methodology.md](docs/methodology.md) for full details.

## Citation

```bibtex
@article{mohammadi2025cultural,
  title={Exploring Cultural Variations in Moral Judgments with Large Language Models},
  author={Mohammadi, Hadi and Giachanou, Anastasia and Oberski, Daniel L. and Bagheri, Ayoub},
  journal={Computational Linguistics in the Netherlands Journal},
  year={2025}
}
```

## License

This project is licensed under the MIT License - see [LICENSE](LICENSE) for details.

## Contact

- **Hadi Mohammadi** - [h.mohammadi@uu.nl](mailto:h.mohammadi@uu.nl)
- Utrecht University, Netherlands

## Acknowledgments

- World Values Survey Association for cross-cultural survey data
- PEW Research Center for Global Attitudes Survey data
- SURF for computational resources
- Anonymous reviewers for valuable feedback
