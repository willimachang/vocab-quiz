import urllib.request
import csv
import io
import sys

# List of potential URLs to try
sources = [
    "https://raw.githubusercontent.com/dyeeee/English-Chinese-Dictionary/master/Common_Words.csv",
    "https://raw.githubusercontent.com/dyeeee/English-Chinese-Dictionary/main/Common_Words.csv",
    # Fallback to a smaller list if above fails (this is a placeholder for a known good local list if we had one)
]

output_file = "vocabulary.csv"

def download_and_parse(url):
    print(f"Attempting to download from: {url}")
    try:
        with urllib.request.urlopen(url) as response:
            content = response.read().decode('utf-8', errors='ignore')
            return content
    except Exception as e:
        print(f"Failed: {e}")
        return None

content = None
for url in sources:
    content = download_and_parse(url)
    if content:
        break

if not content:
    print("All sources failed.")
    sys.exit(1)

print("Download successful. Parsing...")

lines = content.strip().splitlines()
valid_vocab = []

# Try to detect CSV format
# dyeeee/Common_Words.csv usually has columns. Let's inspect first line.
# Assuming standard comma, but some dicts use complex tsv.
# Let's try standard CSV parsing.
# We want to extract just the word and the first Chinese definition.

reader = csv.reader(lines)
header = next(reader, None) # Skip header if it exists? or check it.

# Heuristic: verify if header looks like a header
has_header = False
if header:
    if "word" in header[0].lower() or "english" in header[0].lower():
        has_header = True
    else:
        # Reset reader? No easy way with list iterator, just process header as row if not header
        pass

# If the first row was data, we miss one. But 7000 words, missing one is fine.
# Let's just iterate rest.

for row in reader:
    if not row: continue
    
    # Check robustness
    if len(row) >= 2:
        word = row[0].strip()
        # Some CSVs in that repo might have format: word, phonetic, translation, etc.
        # Let's look for Chinese characters in columns.
        
        translation = ""
        # Find first column with Chinese characters?
        # Or just assume column 1 or 2.
        # Common_Words.csv format is often: word, translation
        
        # Let's assume last column or second column is translation
        potential_trans = row[1] if len(row) > 1 else ""
        
        # Simple check for Chinese characters
        if any('\u4e00' <= char <= '\u9fff' for char in potential_trans):
            translation = potential_trans
        else:
            # Try next columns
            for col in row[2:]:
                if any('\u4e00' <= char <= '\u9fff' for char in col):
                    translation = col
                    break
        
        if word and translation:
            # Clean translation (remove extra definitions separated by ;)
            translation = translation.split(';')[0].split('，')[0]
            valid_vocab.append([word, translation])

print(f"Parsed {len(valid_vocab)} valid words.")

if len(valid_vocab) < 100:
    print("Warning: Parsed count is very low. Might be wrong format.")

# Write to file
try:
    with open(output_file, 'w', encoding='utf-8', newline='') as f:
        writer = csv.writer(f)
        writer.writerow(['word', 'translation'])
        writer.writerows(valid_vocab)
    print(f"Successfully updated {output_file} with {len(valid_vocab)} words.")
except Exception as e:
    print(f"Error writing file: {e}")
