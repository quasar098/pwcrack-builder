from typing import Optional, Union, TextIO, Generator


def get_next_line(file: TextIO, sep="\n") -> Optional[str]:
    """Generator function to read a file line by line"""
    built = ""
    while char := file.read(1):
        if char == sep:
            if built:
                yield built
                built = ""
            continue
        built += char
    if built:
        yield built


def enumerate_list_of_lists(chunks: list[list[str]], remove_duplicates=False, sep="") -> Generator[str, None, None]:
    """Generator function to enumerate over possibilities in list of lists"""
    seen = set()
    enumerator = [0] * len(chunks)
    while True:
        for index, enum in enumerate(enumerator):
            attempt_yield = sep.join([chunk[enumerator[cindex]] for cindex, chunk in enumerate(chunks)])
            if remove_duplicates:
                if attempt_yield not in seen:
                    seen.add(attempt_yield)
                    yield attempt_yield
            else:
                yield attempt_yield
            enumerator[index] += 1
            if enumerator[index] == len(chunks[index]):
                enumerator[index] = 0
                continue
            break
        else:
            break
