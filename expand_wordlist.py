#!/usr/bin/python3

import sys
from typing import Optional, Union, TextIO


def show_usage():
    print("Usage: expand_wordlist.py <infile> [outfile]\nIf outfile is not specified, it prints to stdout")


def usage_checks():
    if len(sys.argv) in (2, 3):
        return True
    show_usage()
    return False


def get_next_line(file: TextIO) -> Optional[str]:
    built = ""
    while char := file.read(1):
        if char == "\n":
            if built:
                yield built
                built = ""
            continue
        built += char
    if built:
        yield built


PRINT_TO_STDOUT = False if len(sys.argv) == 3 else True
new_words = []
registered = []


def register_word(w):
    if REMOVE_DUPLICATES:
        if w in registered:
            return
        registered.append(w)
    if PRINT_TO_STDOUT:
        print(w)
    else:
        new_words.append(w)


def word_variations(w):
    variations = [w]
    if ALTERNATE_CASING:
        try:
            variations.extend([w.lower(), w.upper(), w[0].upper() + w[1:].lower()])
        except IndexError:
            pass
    return variations


REPLACE_NUMBERS = {
    '0': ['0', 'nil', "zero"],
    '1': ['1', 'one'],
    '2': ['2', 'two'],
    '3': ['three', '3'],
    '4': ['four', '4', 'for'],
    '5': ['five', '5'],
    '6': ['six', '6'],
    '7': ['seven', '7'],
    '8': ['eight', '8', 'ate'],
    '9': ['nine', '9']
}


def main():
    if not usage_checks():
        return
    in_file_name = sys.argv[1]
    out_file_name = sys.argv[2] if len(sys.argv) == 3 else None
    with open(in_file_name) as f:
        for line in get_next_line(f):
            # append the original
            register_word(line)

            chunks: list[list[str]] = []
            builder = ""
            for char in line:
                if char.isnumeric():
                    chunks.append(REPLACE_NUMBERS[char])
                    continue
                if char in SPACERS:
                    if builder:
                        chunks.append(word_variations(builder))
                        builder = ""
                    chunks.append(SPACERS)
                else:
                    builder += char
            if builder:
                chunks.append(word_variations(builder))

            incrementors = []
            for _ in chunks:
                incrementors.append(0)

            while True:
                new_word = "".join([chunk[incrementors[index]] for index, chunk in enumerate(chunks)])
                register_word(new_word)
                for index in range(len(incrementors)):
                    incrementors[index] += 1
                    if incrementors[index] == len(chunks[index]):
                        incrementors[index] = 0
                        continue
                    break
                else:
                    break

    if not PRINT_TO_STDOUT:
        with open(out_file_name, "w") as f:
            f.write("\n".join(new_words))


# config
SPACERS = ['-', '', '_']
ALTERNATE_CASING = False
REMOVE_DUPLICATES = True


if __name__ == '__main__':
    main()
