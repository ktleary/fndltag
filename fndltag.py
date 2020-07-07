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


def getlemmas(doc):
    lemmas = []
    for token in doc:
        lemmas.append(token.lemma_.strip().lower())
    return sorted(list(set(lemmas)))


def get_ltags_paths(directory, exts):
    ltags_paths = {}
    filepaths = listfiles(directory, exts)
    for filepath in filepaths:
        with open(filepath) as f:
            content = [i.strip() for i in f.readlines()]
            for line in content:
                tags = tagfind.findall(line)
                doc = nlp(" ".join(tags))
                ltags = getlemmas(doc)
                for ltag in ltags:
                    if not ltags_paths.get(ltag):
                        ltags_paths[ltag] = list(filepath)
                    else:
                        ltags_paths.append(filepath)
        return ltags_paths


def ltag(directory, exts):
    ltags_paths = {}
    # get all matching files from specified directory
    filepaths = listfiles(directory, exts)
    for filepath in filepaths:
        with open(filepath) as f:
            content = [i.strip() for i in f.readlines()]
            for line in content:
                tags = tagfind.findall(line)
                doc = nlp(" ".join(tags))
                ltags = lemmatize(doc)
                for ltag in ltags:
                    if ltags_paths[ltag]:
                        ltags_paths[ltag] = list(filepath)
                    else:
                        ltags_paths.append(filepath)
    return ltags_paths


    # get unique tags
    # tags = tags_paths(files)
    # for tagslist in tagslists:
    #     for tag in tagslist:
    #         tags.append(tag)
    #         tagset = sorted(list(set(tags)))
    # return ltags
    # doc = nlp(" ".join(tagset))
    # lemmas = lemmatize(doc)
    # print(lemmas)


# if __name__ == "__main__":
#     try:
#         sys.exit(main())
#     except FileNotFoundError as e:
#         sys.exit(e)
