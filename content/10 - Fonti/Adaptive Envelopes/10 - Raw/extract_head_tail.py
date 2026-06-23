import glob
import os

out_dir = r"d:\Vaults\Research\Research\10 - Fonti\Adaptive Envelopes\10 - Raw"
for txt_file in glob.glob(os.path.join(out_dir, "*.txt")):
    with open(txt_file, "r", encoding="utf-8") as f:
        content = f.read()
    
    # Take first 15000 and last 15000 characters
    if len(content) > 30000:
        head = content[:15000]
        tail = content[-15000:]
        summary = head + "\n\n... [TESTO TAGLIATO] ...\n\n" + tail
    else:
        summary = content
        
    sum_file = txt_file.replace(".txt", "_summary.txt")
    with open(sum_file, "w", encoding="utf-8") as f:
        f.write(summary)
    print(f"Created {sum_file}")
