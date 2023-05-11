from typing import Optional, Union, TextIO


def _get_next_line(file: TextIO) -> Optional[str]:
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
