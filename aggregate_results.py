import json
import os
import sys

res_dir = "eval_results/minimax-m2.5-nvfp4-longcontext"
summary_files = [f for f in os.listdir(res_dir) if f.endswith("_summary.json")]

total_corr = 0
total_wrong = 0
results = {}

for f in summary_files:
    with open(os.path.join(res_dir, f), 'r') as fi:
        data = json.load(fi)
        # The structure is {"subject": {"corr": ..., "wrong": ..., "acc": ...}, "total": ...}
        # We find the subject key (it's not "total")
        subject = [k for k in data.keys() if k != "total"][0]
        stats = data[subject]
        results[subject] = stats
        total_corr += stats["corr"]
        total_wrong += stats["wrong"]

overall_acc = total_corr / (total_corr + total_wrong) if (total_corr + total_wrong) > 0 else 0

# Console Output
print(f"Overall Accuracy: {overall_acc:.4f}\n")
print(f"| Subject | Accuracy | Correct | Wrong |")
print(f"|---------|----------|---------|-------|")
for sub in sorted(results.keys()):
    stats = results[sub]
    print(f"| {sub.capitalize()} | {stats['acc']:.4f} | {int(stats['corr'])} | {int(stats['wrong'])} |")

# File Output - Markdown
report_path = os.path.join(res_dir, "final_report.md")
with open(report_path, "w") as f:
    f.write(f"# MMLU-Pro Final Report: MiniMax-M2.5-NVFP4\n\n")
    f.write(f"**Overall Accuracy: {overall_acc:.4f}**\n\n")
    f.write(f"| Subject | Accuracy | Correct | Wrong |\n")
    f.write(f"| :--- | :---: | :---: | :---: |\n")
    for sub in sorted(results.keys()):
        stats = results[sub]
        f.write(f"| {sub.capitalize()} | {stats['acc']:.4f} | {int(stats['corr'])} | {int(stats['wrong'])} |\n")
    f.write(f"\n- **Total Correct:** {int(total_corr)}\n")
    f.write(f"- **Total Wrong:** {int(total_wrong)}\n")
    f.write(f"- **Total Questions:** {int(total_corr + total_wrong)}\n")

# File Output - CSV
csv_path = os.path.join(res_dir, "summary_stats.csv")
with open(csv_path, "w") as f:
    f.write("subject,accuracy,correct,wrong\n")
    for sub in sorted(results.keys()):
        stats = results[sub]
        f.write(f"{sub},{stats['acc']:.4f},{int(stats['corr'])},{int(stats['wrong'])}\n")
    f.write(f"total,{overall_acc:.4f},{int(total_corr)},{int(total_wrong)}\n")

print(f"\nFinal report saved to: {report_path}")
print(f"CSV summary saved to: {csv_path}")
