#fndltag

-   Simple script to find and lemmatize hashtags in directory files

## requirements

-   spaCy for nlp

## usage

'''
regex = re.compile('#([\\d\\w]+)')
directory = '/tmp/process'
exts = ['.md', '.txt']

fndltags.ltags_filepaths = fndltag.taglemmas_paths(directory, exts, regex)
'''

example return:
{
"opencollective": [
"/tmp/process/parcel-notes.dv.md"
],
"package": [
"/tmp/process/package-react-component.dv.md",
"/tmp/process/python-modules.dv.md",
"/tmp/process/python-modules.dv.md"
],
"pandoc": [
"/tmp/process/pandoc-batch-convert.dv.md"
],
}

```

## Notes

for standalone purposes, lighter weight tools than spaCy can achieve the same result

Installing en_core_web_sm
```

# download best-matching version of specific model for your spaCy installation

python -m spacy download en_core_web_sm

# pip install .tar.gz archive from path or URL

pip install /Users/you/en_core_web_sm-2.2.0.tar.gz
pip install https://github.com/explosion/spacy-models/releases/download/en_core_web_sm-2.2.0/en_core_web_sm-[version].tar.gz

```

## References

1. spaCy: Industrial-strength NLP: https://github.com/explosion/spaCy
```
