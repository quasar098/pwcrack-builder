# pwcrack-builder

creative idea where you pipe stdout from this program into hashcat or john the ripper instead of making complex rules and stuff

designed to work with a reasonably small wordlist (not rockyou, preferably)

## examples:

Expand wordlist to file

`python3 pwcrack-builder.py expand example/wordlist.txt > expanded-list.txt`

Expand+Enum wordlist to JTR

`python3 pwcrack-builder.py expand+enum example/wordlist.txt | john --pipe --format="Raw-MD5" example/passwords.txt`

Enum+Basic_Cases wordlist to JTR

`python3 pwcrack-builder.py enum+basic_cases example/wordlist.txt | john --format="Raw-MD5" --pipe example/passwords.txt`

## python usage

i am going to build this so that it can be used as a library for convenience

## files

### expand_wordlist.py

- expand a wordlist to account for numbers being words (50 -> fifty)
- account for spacer characters being different ('-', '_', '')
- account for signs like % being represented as "percent" instead

### enumerate.py

- enumerate over common password possibilities when given a wordlist
- add digits, prepend digits
- do digits stuff with letters, special chars
- mix and match

### cases.py

- lower case the entire word, then change 1-4 letters to capital (try all possibilities)
- `The_testing123` can turn into `tHe_tEsTiNG123`

## example/passwords.txt revealed

this tool can crack crazy passwords if you have a good, small wordlist

- `expand`: `blinkonehundredandeighty-two`
- `enum`: `#8cloud92`
- `expand+enum`: `!7Killsninety-nine.nine%OfGerms1`
- `expand+enum2`: `Eblinkonehundredandeighty-two#`
- `cases`: `CityiNtHe-cloUd`
- `expand+cases`: `twEnTyonePilOts`
- `basic_cases+enum`: `XCityinthe-clouDX`
