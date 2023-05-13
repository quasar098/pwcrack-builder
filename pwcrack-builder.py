#!/usr/bin/python3

import sys
from typing import Generator, Callable
from time import time

import src.utils
import src.expand
import src.enumerate
import src.cases

TOOL_MAPPING = {
    "expand": src.expand.expand_password,
    "enumerate": src.enumerate.enumerate_password,
    "cases": src.cases.cases_password,
    "basic_cases": lambda _original: src.cases.cases_password(_original, max_caps=3)
}

TOOL_ALIASES = {
    "enum": "enumerate",
    "exp": "expand",
    "case": "cases",
    "toggle": "cases",
    "caps": "cases",
    "basic_toggle": "basic_cases",
    "basic_caps": "basic_cases"
}

DEBUG = False


# noinspection PyUnusedLocal
def generic_help_message(params: list[str] = None) -> None:
    help_msg = "Usage: python3 pwcrack-builder <tool>(+<tool>)* <filename>"
    help_msg += f"\nPossible tools: {' '.join(TOOL_MAPPING)}"
    print(help_msg)


# noinspection PyArgumentList
def main():
    assert len(sys.argv) != 0, "What? How???"
    if len(sys.argv) != 3:
        generic_help_message()
        quit()

    tools = sys.argv[1].split("+")
    assert len(tools) > 0
    infile = sys.argv[2]

    funcs = []
    for tool in tools:
        funcs.append(TOOL_MAPPING.get(TOOL_ALIASES.get(tool, tool), generic_help_message))

    with open(infile, 'r') as f:
        try:
            before = time()
            new_password_count = 0
            original_wordlist_length = 0
            for line in src.utils.get_next_line(f):
                if line == "":
                    continue
                original_wordlist_length += 1
                if DEBUG:
                    for _ in recursive_generate(line, funcs):
                        new_password_count += 1
                else:
                    for pwd in recursive_generate(line, funcs):
                        print(pwd)
            if DEBUG:
                print(f"Time taken: {time()-before}\n" +
                      f"Total generated: {new_password_count} from {original_wordlist_length}" +
                      f" (~{int(new_password_count/original_wordlist_length)} per original word)\n" +
                      f"Passwords per second: ~{int(new_password_count/(time()-before))}")
        except BrokenPipeError:
            print("Broken Pipe Error: See JTR/Hashcat Output")


def recursive_generate(original: str, funcs: list[Callable]) -> Generator[str, None, None]:
    current_fn, *funcs = funcs
    current_gen = current_fn(original)
    for gen in current_gen:
        if len(funcs):
            for new_gen in recursive_generate(gen, funcs):
                yield new_gen
        else:
            yield gen


if __name__ == '__main__':
    main()
