# MiniMax-M2.5-NVFP4 Benchmark Consolidation Report

This report consolidates results from three variations of the MiniMax-M2.5-NVFP4 model family.

## Executive Summary

| Variation | Accuracy (Overall) | Context Limit (max_tokens) | Notes |
| :--- | :---: | :---: | :--- |
| **NVFP4-32k** | **80.02%** | 32,768 | Original run, highest performance. |
| **MiniMax-M2.5** | **73.13%** | 2,048 | New base model run. |
| **NVFP4-2k** | **69.46%** | 2,048 | Official benchmark settings. |
| **REAP-2k** | **57.24%** | 2,048 | Reasoner-enhanced model (post-fix). |

## Variation Comparison

The follow table compares the accuracy across all benchmark subjects:

| Subject | NVFP4-32k | MiniMax-M2.5 | NVFP4-2k | REAP-2k |
| :--- | :---: | :---: | :---: | :---: |
| biology | 90.24% | 86.61% | 82.98% | 67.64% |
| business | 86.57% | 78.45% | 70.85% | 67.05% |
| chemistry | 87.63% | 76.94% | 72.79% | 54.77% |
| computer science | 85.37% | 76.83% | 75.61% | 67.07% |
| economics | 83.89% | 82.35% | 79.74% | 74.76% |
| engineering | 70.38% | 50.88% | 44.99% | 43.34% |
| health | 78.36% | 75.18% | 74.08% | 37.65% |
| history | 67.19% | 66.40% | 62.47% | 37.53% |
| law | 55.68% | 49.50% | 41.60% | 32.79% |
| math | 93.49% | 84.46% | 81.42% | 74.61% |
| other | 74.89% | 74.03% | 71.54% | 51.62% |
| philosophy | 70.14% | 66.13% | 63.33% | 52.30% |
| physics | 86.76% | 76.67% | 74.60% | 64.28% |
| psychology | 78.20% | 77.82% | 76.82% | 66.92% |
| **Weighted Total** | **80.02%** | **73.13%** | **69.46%** | **57.24%** |

## Key Insights

1. **Impact of Context Length**: Reducing `max_tokens` from 32,768 down to 2,048 resulted in a ~10.5% drop in overall accuracy for the base NVFP4 model. This suggests the model benefits significantly from longer Chain-of-Thought reasoning paths that exceed the 2k limit.
2. **New Base Model Advantage**: The new `MiniMax-M2.5` model achieved 73.13% accuracy with a 2k context, outperforming the previous `NVFP4-2k` run (69.46%).
3. **REAP vs Base**: The REAP-enhanced model performed significantly worse (57.24%) and much slower than the base versions.
4. **Subject Volatility**: Hard sciences (Math, Biology) remained the strongest across all variants, while Law and Engineering suffered more dramatic declines when context or model variants changed.

---
*Consolidated CSV available at: [minimax-m2.5-comparison.csv](file:///home/shihan/Projects/MMLU-Pro/MMLU-Pro/eval_results/minimax-m2.5-comparison.csv)*
