<div align="center">

# Exploring Cultural Variations in Moral Judgments with Large Language Models

[![DOI](https://zenodo.org/badge/DOI/10.5281/zenodo.20090482.svg)](https://doi.org/10.5281/zenodo.20090482)
[![arXiv](https://img.shields.io/badge/arXiv-2506.12433-b31b1b.svg)](https://arxiv.org/abs/2506.12433)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)

*Probing 26 LLMs for cultural moral alignment with the World Values Survey and PEW Global Attitudes data.*

</div>

## Paper

|                  |                                                                          |
| ---------------- | ------------------------------------------------------------------------ |
| **Title**        | Exploring Cultural Variations in Moral Judgments with Large Language Models |
| **Authors**      | Hadi Mohammadi, Robert A. Bagheri |
| **Affiliation**  | Utrecht University, The Netherlands |
| **Venue**        | Computational Linguistics in the Netherlands Journal (in press) |
| **arXiv**        | [2506.12433](https://arxiv.org/abs/2506.12433) |
| **Code archive** | [10.5281/zenodo.20090482](https://doi.org/10.5281/zenodo.20090482) (this repository, snapshot v1.0-thesis) |

> This repository accompanies **Chapter 6** of the PhD thesis
> *Let Me Explain! Explainable NLP for Understanding Large Language Models* (Hadi Mohammadi, Utrecht University, 2026).

## Abstract

Large Language Models increasingly mediate decisions about content moderation, education, and search in culturally diverse contexts, yet their ability to capture moral pluralism is poorly understood. This work evaluates 26 models — from smaller systems (GPT-2, OPT, BLOOMZ, Qwen) to instruction-tuned LLMs (GPT-4o, Gemma, Falcon, Llama-3) — against the World Values Survey (55 countries) and the PEW Global Attitudes Survey (39 countries) across 19 ethical topics. Instruction-tuned models reach moderate alignment with survey data, but a persistent W.E.I.R.D. (Western, Educated, Industrialised, Rich, Democratic) bias remains: alignment with Western European and North American respondents is consistently stronger than with Sub-Saharan African or MENA respondents.

## Citation

If you use this code or data, please cite **both** the paper and this code archive:

```bibtex
@article{mohammadi2026cultural,
  title         = {Exploring Cultural Variations in Moral Judgments with Large Language Models},
  author        = {Mohammadi, Hadi and Bagheri, Robert A.},
  year          = {2026},
  journal       = {Computational Linguistics in the Netherlands Journal},
  eprint        = {2506.12433},
  archivePrefix = {arXiv},
  url           = {https://arxiv.org/abs/2506.12433}
}

@software{mohammadi_cultural_moral_judgments_llms_2026,
  author    = {Mohammadi, Hadi and Bagheri, Robert A.},
  title     = {Exploring Cultural Variations in Moral Judgments with Large Language Models},
  year      = {2026},
  publisher = {Zenodo},
  version   = {v1.0-thesis},
  doi       = {10.5281/zenodo.20090482},
  url       = {https://doi.org/10.5281/zenodo.20090482}
}
```

---

## Key Insight

When asked about the moral acceptability of divorce, an LLM might predict similar attitudes for Sweden and Saudi Arabia—yet survey data reveals nearly opposite positions. Such blind spots matter as LLMs increasingly power content moderation, search engines, and decision-support systems globally.

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
├── README.md
├── SETUP_GUIDE.md
├── LICENSE
├── CITATION.cff
├── requirements.txt
├── paper/
│   └── main.pdf                 # Paper (preprint)
├── src/
│   ├── __init__.py
│   ├── data_processing.py       # Survey data loading and preprocessing
│   ├── model_evaluation.py      # Log-probability moral-justifiability scoring
│   ├── visualization.py         # Plotting utilities
│   └── utils.py                 # Helper functions
├── scripts/
│   ├── run_all_models.py        # Run evaluation on all configured models
│   └── generate_plots.py        # Generate paper figures
└── docs/
    └── methodology.md           # Detailed methodology
```

> **Note:** Survey data (WVS Wave 7, PEW Global Attitudes 2013) is not redistributed in this repo. Obtain it directly from the official sources listed under [Data](#data) below and supply your own paths to the scripts.

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

## License

This project is licensed under the MIT License - see [LICENSE](LICENSE) for details.

## Contact

- **Hadi Mohammadi** — Utrecht University
- Website: [mohammadi.cv](https://mohammadi.cv)

## Acknowledgments

- World Values Survey Association for cross-cultural survey data
- PEW Research Center for Global Attitudes Survey data
- SURF for computational resources
- Anonymous reviewers for valuable feedback
