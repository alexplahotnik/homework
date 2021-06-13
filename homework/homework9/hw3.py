import glob
from pathlib import Path
from typing import Callable, Optional


def my_tokenizer(data):
    """Easy tokenizer logic"""
    yield data


def counter_gen(file):
    """Generator for counting rows"""
    for row in open(file):
        yield row


def universal_file_counter(
    dir_path: Path, file_extension: str, tokenizer: Optional[Callable] = my_tokenizer
) -> int:
    """Function, that counting tokens in some tokenizer logic"""
    count = 0
    filename_list = glob.glob(f"{dir_path}*.{file_extension}")
    print(filename_list)
    for file in filename_list:
        for row in counter_gen(file):
            for token in tokenizer(row):
                count += 1
    return count
