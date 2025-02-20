import pandas as pd

# List of CSV files
files = ["question_tags.csv", "questions.csv"]
chunk_size = 10000  # Read 10,000 rows at a time
count = 0

for file in files:
    for chunk in pd.read_csv(file, dtype=str, chunksize=chunk_size):
        count += chunk.apply(lambda col: col.str.contains("GitHub", case=False, na=False)).any(axis=1).sum()

print(f"Total lines containing 'GitHub': {count}")