import argparse
import collections
import re
import sys
from typing import List, Tuple

def get_most_common_words(text: str, n: int) -> List[Tuple[str, int]]:
    # Case-insensitive: convert to lowercase
    # Punctuation ignored: use regex to find word-like sequences
    words = re.findall(r'\b\w+\b', text.lower())
    counts = collections.Counter(words)
    return counts.most_common(n)

def main():
    parser = argparse.ArgumentParser(description='Print the most common words in a text file.')
    parser.add_argument('filename', help='Path to the text file to analyze')
    parser.add_argument('--top', type=int, default=10, help='Number of most common words to print (default: 10)')
    
    args = parser.parse_args()
    
    try:
        with open(args.filename, 'r', encoding='utf-8') as f:
            text = f.read()
    except FileNotFoundError:
        print(f"Error: File '{args.filename}' not found.", file=sys.stderr)
        sys.exit(1)
    except Exception as e:
        print(f"Error reading file: {e}", file=sys.stderr)
        sys.exit(1)
        
    common_words = get_most_common_words(text, args.top)
    
    for word, count in common_words:
        print(f"{word}: {count}")

if __name__ == "__main__":
    main()
