def getDocumentId(regex, text):
    id = regex.findall(text)
    return id


def main():
    import re
    idfind = re.compile(r'#\s*(\d{12})')
    string = "# 202005010402 Babylonians migrate into Rome, Venice, Constantinople"
    id = getDocumentId(idfind, string)
    if id:
        print(id[0])
    else:
        print("NOTFOUND")


main()
