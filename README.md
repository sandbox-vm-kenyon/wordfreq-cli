# wordfreq

A small Python command-line tool that reads a text file and prints the N most common words.

## Usage

```bash
python wordfreq.py <filename> [--top N]
```

- `<filename>`: The path to the text file you want to analyze.
- `--top N`: (Optional) The number of most common words to display. Defaults to 10.

## Examples

```bash
# Print top 10 common words (default)
python wordfreq.py sample.txt

# Print top 5 common words
python wordfreq.py sample.txt --top 5
```

## Features

- Case-insensitive word counting.
- Ignores punctuation.
- Customizable output limit via `--top`.
