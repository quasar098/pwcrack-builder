# pwcrack-builder

creative idea where you pipe stdout from this program into hashcat or john the ripper instead of making complex rules and stuff

designed to work with a reasonably small wordlist (not rockyou, preferably)

## examples:

Expand wordlist to file

`python3 pwcrack-builder.py expand example/wordlist.txt > expanded-list.txt`

Expand wordlist to JTR

`python3 pwcrack-builder.py expand example/wordlist.txt | john --pipe example/passwords.txt`

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

## example/passwords.txt revealed

this tool can crack crazy passwords if you have a good, small wordlist

- `expand`: `blinkonehundredandeighty-two`
- `enum`: `##DontMindTheStep29`
- `expand&enum`: `!7Killsninety-nine.nine%OfGerms1`
