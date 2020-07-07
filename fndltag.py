import os
import sys
import re
import spacy
nlp = spacy.load("en_core_web_sm")

# hashtag regex
tagfind = re.compile('#([\d\w]+)')

tagslists = []
tags = []


def listfiles(directory: str, patterns: list):
    filepaths = []
    for ROOT, DIR, FILES in os.walk(directory):
        for file in FILES:
            if file.lower().endswith((tuple(patterns))):
                filepaths.append(os.path.join(ROOT, file))
    return sorted(filepaths)


def tags_paths(filepaths):
    tags = []
    for filepath in filepaths:
        with open(filepath) as f:
            content = [i.strip() for i in f.readlines()]
            for line in content:
                tags = tagfind.findall(line)
                if tags:
                    tagslists.append(tags)
        return tags


def getlemmas(doc):
    lemmas = []
    for token in doc:
        lemmas.append(token.lemma_.strip().lower())
    return sorted(list(set(lemmas)))


def ltag(directory, exts):
    ltags = {}
    files = listfiles(directory, exts)

    # tags = tags_paths(files)
    # for tagslist in tagslists:
    # for tag in tagslist:
    # tags.append(tag)
    # tagset = sorted(list(set(tags)))
    return ltags
    # doc = nlp(" ".join(tagset))
    # lemmas = lemmatize(doc)
    # print(lemmas)


# if __name__ == "__main__":
#     try:
#         sys.exit(main())
#     except FileNotFoundError as e:
#         sys.exit(e)
