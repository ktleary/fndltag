import sys
import fndltag
import json


def main():
    import re
    regex = re.compile('#([\\d\\w]+)')
    directory = '/tmp/process'
    exts = ['.md', '.txt']
    ltags_filepaths = fndltag.taglemmas_paths(directory, exts, regex)
    print(json.dumps(ltags_filepaths, indent=4, sort_keys=True))


if __name__ == "__main__":
    try:
        sys.exit(main())
    except FileNotFoundError as e:
        sys.exit(e)
