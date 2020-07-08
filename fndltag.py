import os
import spacy
from typing import Pattern

nlp = spacy.load("en_core_web_sm")


def listfiles(directory: str, patterns: list):
    filepaths = []
    for ROOT, DIR, FILES in os.walk(directory):
        for file in FILES:
            if file.lower().endswith((tuple(patterns))):
                filepaths.append(os.path.join(ROOT, file))
    return sorted(filepaths)


def lemmatize(doc):
    lemmas = []
    for token in doc:
        lemmas.append(token.lemma_.strip().lower())
    return list(set(lemmas))


def taglemmas_paths(directory: str, exts: list, tag_regex: Pattern):
    tlp = {}
    filepaths = listfiles(directory, exts)
    for filepath in filepaths:
        with open(filepath) as f:
            content = [i.strip() for i in f.readlines()]
            for line in content:
                tags = tag_regex.findall(line)
                doc = nlp(" ".join(tags))
                ltags = lemmatize(doc)
                for ltag in ltags:
                    if not tlp.get(ltag):
                        tlp[ltag] = [filepath]
                    else:
                        tlp[ltag].append(filepath)
    return tlp
