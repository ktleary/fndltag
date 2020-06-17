import sys
import re
import spacy
from util import getOptions, listFiles
nlp = spacy.load("en_core_web_sm")

tagfind = re.compile('#([\d\w]+)')
tagslists = []
tags = []
tagsLemmasPaths = {}


def findConnectedTags(tagdict):
    for d in tagdict:
        if len(tagdict[d]) > 1:
            print(d, tagdict[d])


def updateTagsLemmasPaths(filepath, tags):
    tagstr = " ".join(tags)
    tagdoc = nlp(tagstr)
    taglemmas = lemmatize(tagdoc)
    for taglemma in taglemmas:
        if taglemma not in tagsLemmasPaths:
            tagsLemmasPaths[taglemma] = [filepath]
        else:
            # print("Found existing tag: " + taglemma)
            tagsLemmasPaths[taglemma].append(filepath)
            # print(tagsLemmasPaths[taglemma])


def findTags(filepaths):
    for filepath in filepaths:
        filetags = []
        with open(filepath) as f:
            content = [i.strip() for i in f.readlines()]
            for line in content:
                tags = tagfind.findall(line)
                if tags:
                    tagslists.append(tags)
                    for tag in tags:
                        filetags.append(tag)
            updateTagsLemmasPaths(filepath, filetags)


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
    # print(lemmas)
    # tagsLemmasPaths
    findConnectedTags(tagsLemmasPaths)


if __name__ == "__main__":
    try:
        sys.exit(main())
    except FileNotFoundError as e:
        sys.exit(e)
"""
# References
1. mod_structured/createJsonld.py
2. command: python slipbox-tag-find.py -d ./data -p *.md
"""
