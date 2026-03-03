# MMLU-Pro Final Report: MiniMax-M2.5-NVFP4

**Overall Accuracy: 0.8002**

| Subject | Accuracy | Correct | Wrong |
| :--- | :---: | :---: | :---: |
| Biology | 0.9024 | 647 | 70 |
| Business | 0.8657 | 683 | 106 |
| Chemistry | 0.8763 | 992 | 140 |
| Computer science | 0.8537 | 350 | 60 |
| Economics | 0.8389 | 708 | 136 |
| Engineering | 0.7038 | 682 | 287 |
| Health | 0.7836 | 641 | 177 |
| History | 0.6719 | 256 | 125 |
| Law | 0.5568 | 613 | 488 |
| Math | 0.9349 | 1263 | 88 |
| Other | 0.7489 | 692 | 232 |
| Philosophy | 0.7014 | 350 | 149 |
| Physics | 0.8676 | 1127 | 172 |
| Psychology | 0.7820 | 624 | 174 |

- **Total Correct:** 9628
- **Total Wrong:** 2404
- **Total Questions:** 12032

## Comparison: Repository compute_accuracy.py (Level 2)

> [!NOTE]
> The repository script includes a random-guess fallback (1-in-10 chance) for unparsed answers, which may result in slightly higher scores compared to the strict regrading logic.

**Weighted Overall Accuracy: 0.8012**

| Subject | Accuracy (Repo Script) |
| :--- | :---: |
| Biology | 0.9038 |
| Business | 0.8669 |
| Chemistry | 0.8790 |
| Computer science | 0.8537 |
| Economics | 0.8389 |
| Engineering | 0.7069 |
| Health | 0.7836 |
| History | 0.6719 |
| Law | 0.5577 |
| Math | 0.9356 |
| Other | 0.7489 |
| Philosophy | 0.7014 |
| Physics | 0.8691 |
| Psychology | 0.7820 |
