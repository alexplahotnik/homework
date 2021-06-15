import sys


def my_precious_logger(text: str):
    if not text.find("error"):
        sys.stderr.write(text)
    else:
        sys.stdout.write(text)
