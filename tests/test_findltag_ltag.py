import tempfile
import spacy
from pathlib import Path
from unittest import TestCase
import fndltag
import json

nlp = spacy.load("en_core_web_sm")


class TestLtags(TestCase):
    def setUp(self):
        self.name = 'test ltags'
        self.tmpdir = tempfile.TemporaryDirectory()
        self.exts = ['.md', '.txt']
        self.filenames = [
            'markdown1.md', 'markdown2.md', 'markdown3.md', 'text1.txt',
            'text2.txt', 'text3.txt'
        ]
        self.words = "tagging tag labels label control"
        self.doc = "# Title 1 \n #tagging, #labels, #tag, #label, #control"

    def test_ltags_returntype(self):
        # test pholoc findExifFile return type is dictionary
        result = fndltag.ltag(self.tmpdir.name, self.exts)
        self.assertEqual(True, isinstance(result, dict))

    def test_lemmatize(self):
        doc = nlp(self.words)
        lemmas = fndltag.getlemmas(doc)
        self.assertEqual(True, "tag" in lemmas and "tagging" not in lemmas)

    # def test_lemmatize(self):
    # with tempfile.TemporaryDirectory as fp:
    # with tempfile.TemporaryFile() as fp:
    # fp.write(self.doc)


class TestListFiles(TestCase):
    def test_listfiles(self):
        with tempfile.TemporaryDirectory() as tmpdirname:
            filepaths = []
            basename = "test1"

            ext = ".txt"
            for i in range(5):
                path = Path(tmpdirname, basename + str(i) + ext)
                path.touch()
                filepaths.append(str(path))

            ext = ".md"
            for i in range(5, 10):
                path = Path(tmpdirname, basename + str(i) + ext)
                path.touch()
                filepaths.append(str(path))

            files_found = fndltag.listfiles(tmpdirname, ['.txt', '.md'])
            self.assertEqual(filepaths, files_found)


'''
with TemporaryDirectory() as tmpdirname:
        ext = ".md"
        basename = "201906242157"
        filepaths = []
        for i in range(3):
            path = Path(tmpdirname, basename + str(i) + ext)
            path.touch()
            filepaths.append(str(path))


>>> import tempfile

# create a temporary file and write some data to it
>>> fp = tempfile.TemporaryFile()
>>> fp.write(b'Hello world!')
# read data from file
>>> fp.seek(0)
>>> fp.read()
b'Hello world!'
# close the file, it will be removed
>>> fp.close()

# create a temporary file using a context manager
>>> with tempfile.TemporaryFile() as fp:
...     fp.write(b'Hello world!')
...     fp.seek(0)
...     fp.read()
b'Hello world!'
>>>
# file is now closed and removed

# create a temporary directory using the context manager
>>> with tempfile.TemporaryDirectory() as tmpdirname:
...     print('created temporary directory', tmpdirname)
>>>
# directory and contents have been removed
'''
