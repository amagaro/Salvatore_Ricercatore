import os

text = "This is a test document to see if text ingestion works in NotebookLM."
with open("test_ingest.txt", "w") as f:
    f.write(text)
