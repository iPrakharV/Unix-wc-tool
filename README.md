# Unix Word Counter

`wc` is a Python-based command-line tool that replicates some of the functionalities of the Unix `wc` utility. This tool allows users to count bytes, words, lines, and characters in a given text file or standard input.

## Features

- Count the number of bytes in the text.
- Count the number of lines in the text.
- Count the number of words in the text.
- Count the number of characters in the text.
- Read input from a file or standard input.

## Installation

Clone this repository to your local machine:

```bash
https://github.com/iPrakharV/Unix-wc-tool.git
```
Navigate to the cloned directory:
```bash
cd wc
```
## Usage
To use pywc, you can pass in a filename or pipe text into it from standard input. Here are some examples of how to use pywc:
```bash
# Count lines, words, and characters in a file
python3 wc.py test.txt

# Count only lines from standard input
cat test.txt | python3 wc.py -l

# Count only words in a file
python3 wc.py -w test.txt

# Count only characters in a file
python3 wc.py -m test.txt

# Count only bytes in a file
python3 wc.py -c test.txt
```
## Options
- -c, --bytes Count the number of bytes.
- -l, --lines Count the number of lines.
- -w, --words Count the number of words.
- -m, --chars Count the number of characters.
## Contributing
Contributions are welcome! Please feel free to submit a pull request or open an issue if you have suggestions or improvements.