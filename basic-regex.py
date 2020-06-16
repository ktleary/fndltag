import sys
import re


def matchPattern(pattern, text):
    result = re.match(pattern, text)
    if result:
        print(result.span())
        return True
    return False


def splitText(pattern, text):
    pieces = re.split(pattern, text)
    return pieces


def findAll(pattern, text):
    result = re.findall(pattern, text)
    return result


def substitute(patt, repl, text):
    result = re.sub(patt, repl, text)
    return result


def searchText(patt, text):
    match = re.search(patt, text)
    return match


def matchGroup(patt, text):
    match = re.search(patt, text)
    return match.group() if True else "Pattern not found."


def main():
    pattern = '^a...s$'
    texts = ['abyss', 'abe']
    for text in texts:
        result = matchPattern(text, pattern)
        print(result)
    pattern = '[s]'
    for text in texts:
        result = matchPattern(text, pattern)
        print(result)
    string = 'hello 12 hi 89. Howdy 34'
    pattern = '\d+'
    result = findAll(string, pattern)
    print(result)
    string = 'Twelve:12 Eighty nine:89.'
    pattern = '\d+'
    result = splitText(pattern, string)
    print(result)
    pattern = '\#'
    string = '#bob, #charly, #elephant3, #dog'
    result = splitText(pattern, string)
    print(result)
    print(result)
    string = "Pythonx is fun"
    pattern = 'Python'
    result = searchText(pattern, string)
    print("found" if result else "not found")
    pattern = '(\d{3}) (\d{2})'
    string = '39801 356, 2102 1111'
    result = matchGroup(pattern, string)
    print(result)
    string = 'abc 12\
de 23 \n f45 6'

    pattern = '\s+'
    repl = ''
    result = substitute(pattern, repl, string)


if __name__ == "__main__":
    try:
        sys.exit(main())
    except FileNotFoundError as e:
        sys.exit(e)
"""
#  References
1. Python RegEx: https://www.programiz.com/python-programming/regex

"""
