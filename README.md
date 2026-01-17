# Cultural Moral Judgments in Large Language Models

This repository contains materials for our research on exploring how Large Language Models represent and align with cultural variations in moral judgments across different societies.

## Paper

**Title:** Exploring Cultural Variations in Moral Judgments with Large Language Models

**Authors:** Hadi Mohammadi, Anastasia Giachanou, Ayoub Bagheri

**Affiliation:** Utrecht University, The Netherlands

**arXiv:** [2506.12433](https://arxiv.org/abs/2506.12433)

## Overview

We investigate whether LLMs can capture the nuanced moral reasoning patterns that vary across cultures and contexts, using data from the World Values Survey (WVS) spanning 55+ countries.

## Key Findings

- Large language models show significant alignment with human moral judgments (r > 0.85 for top-tier models)
- Performance varies substantially across cultural contexts
- Western-centric training data leads to better alignment with Western moral norms
- Larger models generally show better cross-cultural alignment

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
└── README.md
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
- Website: [mohammadi-hadi.github.io](https://mohammadi-hadi.github.io)
