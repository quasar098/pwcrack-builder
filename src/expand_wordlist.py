import src.utils
import argparse
from typing import TextIO, Generator
import num2words


COMMON_REPLACEMENT = {
    "@": ["at"],
    "#": ["hashtag"],
    "$": ["money"],
    "%": ["percent"],
    "&": ["and"],
    "*": ["times", "star"],
    "-": ["minus"],
    "+": ["plus"]
}


def expand_wordlist_argparse(params: list[str] = "") -> None:
    parser = argparse.ArgumentParser(add_help=False, usage=argparse.SUPPRESS)
    parser.add_argument("infile", type=str)
    namespace = parser.parse_args(params)
    with open(namespace.infile, 'r') as infile:
        for new_word in expand_wordlist(infile):
            print(new_word)


def expand_wordlist(infile: TextIO) -> Generator[str, None, None]:
    """Generator function that takes a file as input and yields an expanded word for each output"""
    for line in src.utils.get_next_line(infile):
        for expanded in expand_password(line, remove_duplicates=True):
            yield expanded


def expand_password(original: str, remove_duplicates=True) -> Generator[str, None, None]:
    """Expand a singular password into multiple via this generator function"""
    seen = {original}
    yield original
    chunks = []
    builder = ""
    curr_type = "normal"  # normal, number

    def add_builder():
        nonlocal builder
        if builder in ("_", '-'):
            chunks.append(["_", '-', ''])
            builder = ""
            return
        elif builder in COMMON_REPLACEMENT:
            chunks.append([builder] + list(COMMON_REPLACEMENT.get(builder, [])))
            builder = ""
            return
        elif builder.isnumeric():
            worded = num2words.num2words(int(builder)).replace(" ", "")
            better_worded = "".join([num2words.num2words(int(n)) for n in builder])
            chunks.append([
                builder,
                worded,
                worded.replace("and", ''),
                worded.replace("-", ''),
                worded.replace("and", '').replace("-", ''),
                better_worded
            ])
            builder = ""
            return
        else:
            chunks.append([builder])
            builder = ""
            return

    for char in original:
        if char in ("_", "-", ''):
            add_builder()
        elif char in COMMON_REPLACEMENT:
            add_builder()
        elif char.isnumeric() and curr_type != "number":
            curr_type = "number"
            add_builder()
        elif not char.isnumeric() and curr_type != "normal":
            curr_type = "normal"
            add_builder()

        builder += char
    add_builder()
    for new in src.utils.enumerate_list_of_lists(chunks, remove_duplicates=remove_duplicates):
        if new not in seen:
            yield new
            seen.add(new)
