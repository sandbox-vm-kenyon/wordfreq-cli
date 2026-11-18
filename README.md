# wordfreq

A small Python command-line tool that reads a text file and prints the N most common words with their counts.

## Installation

Simply clone the repository and ensure you have Python 3 installed.

```bash
git clone https://github.com/sandbox-vm-kenyon/wordfreq-cli.git
cd wordfreq-cli
```

## Usage

The `wordfreq` tool takes a file path as a positional argument and an optional `--top` argument to specify how many of the most frequent words to display.

```bash
python wordfreq.py <filename> [--top N]
```

- `<filename>`: The path to the text file to analyze.
- `--top N`: (Optional) The number of most common words to display. Defaults to 10.

## Examples

### Example 1: Default Usage (Top 10)
If you have a file named `sample.txt` containing:
*"The cat sat on the mat. The dog sat on the rug."*

```bash
python wordfreq.py sample.txt
```

**Expected Output:**
```text
the: 4
sat: 2
on: 2
cat: 1
mat: 1
dog: 1
rug: 1
```

### Example 2: Custom Limit (Top 3)
```bash
python wordfreq.py sample.txt --top 3
```

**Expected Output:**
```text
the: 4
sat: 2
on: 2
```

## Features

- **Case-Insensitive**: "The" and "the" are counted as the same word.
- **Punctuation Ignored**: Words are extracted using alphanumeric sequences, ignoring periods, commas, and other punctuation.
- **Customizable Limit**: Control the output size using the `--top` flag.
