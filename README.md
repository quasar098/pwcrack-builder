# pwcrack-builder

creative idea where you pipe stdout from this program into hashcat or john the ripper instead of making complex rules and stuff

## examples:

Expand wordlist to file

`python3 pwcrack-builder.py expand example/wordlist.txt > expanded-list.txt`

Expand wordlist to JTR

`python3 pwcrack-builder.py expand example/wordlist.txt | john --pipe passwords.txt`

## python usage

i am going to build this so that it can be used as a library for convenience

## files

### expand_wordlist.py

expand a wordlist to account for numbers being words and a few other things too
