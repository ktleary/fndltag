import os
import argparse

directoryHelp = "Fully qualified location of the directory to inspect."
reportHelp = "File location for report"
patternHelp = "Pattern to match files. Repeat to match multiple file types."
reportLocation = '/tmp/tags.txt'


def listFiles(directory, patterns="*.*"):
    filepaths = []
    for ROOT, DIR, FILES in os.walk(directory):
        for file in FILES:
            if file.endswith((tuple(patterns))):
                filepaths.append(os.path.join(ROOT, file))
    return sorted(filepaths)


def getOptions(args):
    parser = argparse.ArgumentParser(description="Parser")
    parser.add_argument("-d", "--directory", default=".", help=directoryHelp)
    parser.add_argument("-r",
                        "--report",
                        default=reportLocation,
                        help=reportHelp)
    parser.add_argument("-p",
                        "--pattern",
                        default=["*.*"],
                        action="append",
                        help=patternHelp),

    options = parser.parse_args(args)
    return options
