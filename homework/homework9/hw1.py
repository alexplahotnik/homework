from pathlib import Path
from typing import Iterator, List, Union


def merge_sorted_files(file_list: List[Union[Path, str]]) -> Iterator:
    "Function, that merges integers from files and return then in iterator"
    result = []
    for file in file_list:
        with open(file) as f:
            for number in f.readlines():
                result.append(int(number.rstrip()))
    return iter(sorted(result))
