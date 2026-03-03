import os
import re

def parse_repo_output(output_file):
    results = {}
    with open(output_file, 'r') as f:
        content = f.read()
    
    # Each subject has a Level 1 and Level 2 block
    # We want the Level 2 score
    blocks = content.split('Level 2 regex========================================')
    for block in blocks[1:]:
        lines = block.strip().split('\n')
        if lines:
                # Handle spaces in filenames (e.g., 'computer science_result.json')
                # The line format is path score
                # We can split from the right
                parts = lines[0].rsplit(None, 1)
                if len(parts) == 2:
                    file_path = parts[0]
                    acc = float(parts[1])
                    subject = os.path.basename(file_path).replace('_result.json', '')
                    results[subject] = acc
    return results

def main():
    res_dir = "eval_results/minimax-m2.5-nvfp4-longcontext"
    repo_results = parse_repo_output("repo_script_output.txt")
    
    # Question counts per subject for weighted average
    counts = {
        "biology": 717, "business": 789, "chemistry": 1132, "computer science": 410,
        "economics": 844, "engineering": 969, "health": 818, "history": 381,
        "law": 1101, "math": 1351, "other": 924, "philosophy": 499,
        "physics": 1299, "psychology": 798
    }
    
    total_q = sum(counts.values())
    weighted_acc = sum(repo_results[s] * counts[s] for s in repo_results) / total_q
    
    # Append to final_report.md
    report_path = os.path.join(res_dir, "final_report.md")
    with open(report_path, "a") as f:
        f.write("\n## Comparison: Repository compute_accuracy.py (Level 2)\n\n")
        f.write("> [!NOTE]\n")
        f.write("> The repository script includes a random-guess fallback (1-in-10 chance) for unparsed answers, which may result in slightly higher scores compared to the strict regrading logic.\n\n")
        f.write(f"**Weighted Overall Accuracy: {weighted_acc:.4f}**\n\n")
        f.write("| Subject | Accuracy (Repo Script) |\n")
        f.write("| :--- | :---: |\n")
        for sub in sorted(repo_results.keys()):
            f.write(f"| {sub.capitalize()} | {repo_results[sub]:.4f} |\n")
            
    # Append to summary_stats.csv
    csv_path = os.path.join(res_dir, "summary_stats.csv")
    with open(csv_path, "a") as f:
        f.write("\n# Comparison Data: Repository compute_accuracy.py (Level 2)\n")
        f.write("subject,accuracy,method\n")
        for sub in sorted(repo_results.keys()):
            f.write(f"{sub},{repo_results[sub]:.4f},repo_script_l2\n")
        f.write(f"total,{weighted_acc:.4f},repo_script_l2\n")

    print(f"Comparison data appended to {report_path} and {csv_path}")

if __name__ == "__main__":
    main()
