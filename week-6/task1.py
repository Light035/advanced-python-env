import string
from pathlib import Path

BASE_DIR = Path(__file__).parent

def analyze_text(input_file, output_file):
    word_freq = {}
    lines_count = 0
    words_count = 0

    with open(input_file, 'r', encoding='utf-8') as f:
        for line in f:
            lines_count += 1
            line = line.lower()
            line = line.translate(str.maketrans('', '', string.punctuation))
            words = line.split()
            words_count += len(words)

            for word in words:
                word_freq[word] = word_freq.get(word, 0) + 1

    with open(output_file, 'w', encoding='utf-8') as f:
        f.write(f"Lines: {lines_count}\n")
        f.write(f"Words: {words_count}\n")
        f.write("Word frequency:\n")
        for word, count in word_freq.items():
            f.write(f"{word}: {count}\n")


analyze_text(
    BASE_DIR / "text.txt",
    BASE_DIR / "analysis.txt"
)
import string
from pathlib import Path

BASE_DIR = Path(__file__).parent

def analyze_text(input_file, output_file):
    word_freq = {}
    lines_count = 0
    words_count = 0

    with open(input_file, 'r', encoding='utf-8') as f:
        for line in f:
            lines_count += 1
            line = line.lower()
            line = line.translate(str.maketrans('', '', string.punctuation))
            words = line.split()
            words_count += len(words)

            for word in words:
                word_freq[word] = word_freq.get(word, 0) + 1

    with open(output_file, 'w', encoding='utf-8') as f:
        f.write(f"Lines: {lines_count}\n")
        f.write(f"Words: {words_count}\n")
        f.write("Word frequency:\n")
        for word, count in word_freq.items():
            f.write(f"{word}: {count}\n")


analyze_text(
    BASE_DIR / "text.txt",
    BASE_DIR / "analysis.txt"
)
