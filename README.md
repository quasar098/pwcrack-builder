# pwcrack-builder

creative idea (not that practical but whatever) where you pipe stdout from this program into hashcat or john the ripper instead of making complex rules and stuff

designed to work with a reasonably small wordlist (not rockyou, preferably), and with extremely specific requirements (e.g. reverse the first 4 characters of the word unless the word is in the english dictionary)

## examples:

Expand wordlist to file

`python3 pwcrack-builder.py expand example/wordlist.txt > expanded-list.txt`

Expand+Enum wordlist to JTR

`python3 pwcrack-builder.py expand+enum example/wordlist.txt | john --pipe --format="Raw-MD5" example/passwords.txt`

Enum+Basic_Cases wordlist to JTR

`python3 pwcrack-builder.py enum+basic_cases example/wordlist.txt | john --format="Raw-MD5" --pipe example/passwords.txt`

## python usage

i am going to build this so that it can be used as a library for convenience

## speed

not fast<br>
i tried using multiprocessing module but it was still slow<br>
maybe you could use this to generate rulesets idk<br>
can do `basic_cases+expand+enum` for a 1k length wordlist in ~24 hours (estimated) 

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
- alternatively use `basic_cases` for 1-2 letters to capital

## it isn't working !11!1

use `+debug` at the end of your tool chain/tool list to print out stats. do not use debug with pipe or redirect!!

## example/passwords.txt revealed

this tool can crack crazy passwords if you have a good, small wordlist

- `expand`: `blinkonehundredandeighty-two`
- `enum`: `#8cloud92`
- `expand+enum`: `!7Killsninety-nine.nine%OfGerms1`
- `expand+enum2`: `Eblinkonehundredandeighty-two#`
- `cases`: `CityiNtHe-cloUd`
- `expand+cases`: `twEnTyonePilOts`
- `basic_cases+enum`: `XCityinthe-clouDX`
- `basic_cases+enum2`: `5carriE_uNderwood9a`
