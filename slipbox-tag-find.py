import sys
import re
import spacy
from util import getOptions, listFiles
nlp = spacy.load("en_core_web_sm")

tagfind = re.compile('#([\d\w]+)')
tagslists = []
tags = []


def findTags(filepaths):
    for filepath in filepaths:
        with open(filepath) as f:
            content = [i.strip() for i in f.readlines()]
            for line in content:
                tags = tagfind.findall(line)
                if tags:
                    tagslists.append(tags)


def lemmatize(doc):
    lemmas = []
    for token in doc:
        lemmas.append(token.lemma_.strip().lower())
    return sorted(list(set(lemmas)))


def main():
    options = getOptions(sys.argv[1:])
    files = listFiles(options.directory, "*.md")
    findTags(files)
    for tagslist in tagslists:
        for tag in tagslist:
            tags.append(tag)
    tagset = sorted(list(set(tags)))
    doc = nlp(" ".join(tagset))
    lemmas = lemmatize(doc)
    print(lemmas)


if __name__ == "__main__":
    try:
        sys.exit(main())
    except FileNotFoundError as e:
        sys.exit(e)
