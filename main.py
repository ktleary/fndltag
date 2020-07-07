from hconfig.py import directories

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
