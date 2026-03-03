import os
import json
import re
import random

# Advanced extraction logic from compute_accuracy.py
def extract_answer(text):
    # Level 1 regex
    pattern_l1 = r"answer is \(?([A-J])\)?"
    match = re.search(pattern_l1, text)
    if match:
        return match.group(1)
    
    # Level 2 regex / extract_again
    match = re.search(r'.*[aA]nswer:\s*([A-J])', text)
    if match:
        return match.group(1)
    
    # extract_final
    pattern_final = r"\b[A-J]\b(?!.*\b[A-J]\b)"
    match = re.search(pattern_final, text, re.DOTALL)
    if match:
        return match.group(0)
    
    return None

def regrade_subject(res_dir, subject_file):
    with open(os.path.join(res_dir, subject_file), 'r') as f:
        data = json.load(f)
    
    updated = False
    corr, wrong = 0, 0
    subject = None
    
    for entry in data:
        if subject is None:
            subject = entry.get("category")
            
        old_pred = entry.get("pred")
        model_output = entry.get("model_outputs")
        
        if model_output:
            new_pred = extract_answer(model_output)
        else:
            new_pred = None
            
        if new_pred != old_pred:
            entry["pred"] = new_pred
            updated = True
        
        if new_pred == entry["answer"]:
            corr += 1
        else:
            wrong += 1
            
    if updated:
        with open(os.path.join(res_dir, subject_file), 'w') as f:
            json.dump(data, f)
            
    # Update summary
    if subject:
        summary_file = subject_file.replace("_result.json", "_summary.json")
        acc = corr / (corr + wrong) if (corr + wrong) > 0 else 0
        summary_data = {
            subject: {"corr": float(corr), "wrong": float(wrong), "acc": acc},
            "total": {"corr": float(corr), "wrong": float(wrong), "acc": acc}
        }
        with open(os.path.join(res_dir, summary_file), 'w') as f:
            json.dump(summary_data, f)
            
    return updated, corr, wrong

def main():
    res_dir = "eval_results/minimax-m2.5-nvfp4-longcontext"
    result_files = [f for f in os.listdir(res_dir) if f.endswith("_result.json")]
    
    total_corr = 0
    total_wrong = 0
    
    print(f"Regrading {len(result_files)} subjects...")
    for f in result_files:
        _, corr, wrong = regrade_subject(res_dir, f)
        total_corr += corr
        total_wrong += wrong
        print(f"  Processed {f}: {corr} correct, {wrong} wrong.")
        
    overall_acc = total_corr / (total_corr + total_wrong) if (total_corr + total_wrong) > 0 else 0
    print(f"\nFinal Regraded Accuracy: {overall_acc:.4f}")

if __name__ == "__main__":
    random.seed(12345)
    main()
