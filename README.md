# Python Document Statistics

## Project Overview

This project is a Python-based text analysis program
developed to read text files, calculate word counts,
and identify the most frequently occurring words.

The program demonstrates file handling, string
manipulation, dictionaries, and basic data analysis
using Python.

## Technologies Used

- Python 3
- Python Standard Library
- File Input/Output
- Dictionaries
- String Manipulation

## Features

- Reads text files using Python file operations.
- Calculates the total number of words in a document.
- Removes punctuation and converts text to lowercase.
- Filters common stop words from frequency analysis.
- Counts word occurrences using a dictionary.
- Sorts words by frequency.
- Displays the 10 most frequently occurring words.
- Checks whether a filename was provided.

## How It Works

1. The user provides a text file as a command-line argument.
2. The program opens and reads the file.
3. Punctuation is removed and words are converted to lowercase.
4. The total word count is calculated.
5. Common stop words are excluded from frequency analysis.
6. Word frequencies are stored in a dictionary.
7. The 10 most frequent words are displayed.

## How to Run the Program

### Requirements

- Python 3 installed
- A plain text file (.txt)

### Instructions

1. Download `documentstats.py` from this repository.
2. Place a text file in the same folder as the script.
3. Open a terminal in that folder.
4. Run the following command:

```python
python documentstats.py filename.txt
