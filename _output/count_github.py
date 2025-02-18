
import pandas as pd

# Define the correct CSV file names
files = ["../question_tags.csv", "../questions.csv"]  # Update file names as needed
count = 0

for file in files:
    try:
        df = pd.read_csv(file, encoding='utf-8', on_bad_lines='skip')  # Read CSV safely
        count += df.apply(lambda row: row.astype(str).str.contains("GitHub", case=False, na=False).any(), axis=1).sum()
    except FileNotFoundError:
        print(f"Warning: {file} not found.")
    except Exception as e:
        print(f"Error processing {file}: {e}")

print(f"Total lines containing 'GitHub': {count}")
