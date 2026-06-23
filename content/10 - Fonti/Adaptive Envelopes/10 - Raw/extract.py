import os
import glob
import fitz

out_dir = r"d:\Vaults\Research\Research\10 - Fonti\Adaptive Envelopes\10 - Raw"
for pdf_file in glob.glob(os.path.join(out_dir, "*.pdf")):
    txt_file = pdf_file.replace(".pdf", ".txt")
    if not os.path.exists(txt_file):
        try:
            doc = fitz.open(pdf_file)
            text = "\n".join([page.get_text() for page in doc])
            with open(txt_file, "w", encoding="utf-8") as f:
                f.write(text)
            print(f"Extracted {len(text)} characters from {pdf_file}")
        except Exception as e:
            print(f"Failed {pdf_file}: {e}")
