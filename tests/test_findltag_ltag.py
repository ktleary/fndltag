import tempfile
import spacy
import re
from pathlib import Path
from unittest import TestCase
import fndltag

nlp = spacy.load("en_core_web_sm")


class TestLemmTagPaths(TestCase):
    def setUp(self):
        self.tag_regex = re.compile('#([\\d\\w]+)')
        self.exts = ['.md', '.txt']

    def test_isdict(self):
        directory = tempfile.TemporaryDirectory()
        result = fndltag.taglemmas_paths(directory.name, self.exts,
                                         self.tag_regex)
        self.assertEqual(True, isinstance(result, dict))

    def test_lemmatize(self):
        words = "tagging tag labels label control"
        doc = nlp(words)
        lemmas = fndltag.lemmatize(doc)
        self.assertEqual(True, "tag" in lemmas and "tagging" not in lemmas)

    def test_ltags_paths(self):
        basename = "test"
        testext = ".md"
        tagged_doc = '# Title 1 \n #tagging, #labels, #tag, #label'

        with tempfile.TemporaryDirectory() as tmpdirname:
            path = Path(tmpdirname, str(basename) + testext)
            with open(path, mode='a') as tag_file:
                tag_file.write(tagged_doc)
                tag_file.close()

            ltag_paths = fndltag.taglemmas_paths(tmpdirname, self.exts,
                                                 self.tag_regex)
            self.assertEqual(True, str(path) in ltag_paths["tag"])
            self.assertEqual(True, "labels" not in ltag_paths)


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
