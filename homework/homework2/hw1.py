"""
Given a file containing text. Complete using only default collections:
    1) Find 10 longest words consisting from largest amount of unique symbols
    2) Find rarest symbol for document
    3) Count every punctuation char
    4) Count every non ascii char
    5) Find most common non ascii char for document
"""
import string
from typing import List


def get_longest_diverse_words(file_path: str) -> List[str]:
    with open(file_path, encoding="unicode_escape") as f:
        text = f.read()
        f.close()
    punctuation = [".", ",", "!", "?", ":", ";", "'", "...", "(", ")", "-\n", "-"]
    for punc_char in punctuation:
        text = text.replace(punc_char, "")
    text = text.replace("\n", " ")
    words = text.split(" ")
    unique = {}
    for word in words:
        unique[word] = len(set(word)), len(word)
    sorted_key = sorted(unique, key=unique.get, reverse=True)
    return sorted_key[:10]


def get_rarest_char(file_path: str) -> List:
    with open(file_path, encoding="unicode_escape") as f:
        text = f.read()
        f.close()
    chars = set(text)
    rarest_char = [text[0]]
    count = text.count(text[0])
    for char in chars:
        if text.count(char) < count:
            count = text.count(char)
            rarest_char = [char]
        elif text.count(char) == count:
            rarest_char.append(char)
    return rarest_char


def count_punctuation_chars(file_path: str) -> int:
    with open(file_path, encoding="unicode_escape") as f:
        text = f.read()
        f.close()
    count_punctations = 0
    punctuation = string.punctuation + "»«—’"
    for char in punctuation:
        count_punctations += text.count(char)
    return count_punctations


def count_non_ascii_chars(file_path: str) -> int:
    with open(file_path, encoding="unicode-escape") as f:
        text = f.read()
        f.close()
    count = 0
    for char in text:
        if char not in string.printable:
            count += 1
    return count


def get_most_common_non_ascii_char(file_path: str) -> List:
    with open(file_path, encoding="unicode-escape") as f:
        text = f.read()
        f.close()
    chars = set(text)
    count_max = 0
    common_char = [text[0]]
    for char in chars:
        if char not in string.printable:
            if text.count(char) > count_max:
                count_max = text.count(char)
                common_char = [char]
            elif text.count(char) == count_max:
                common_char.append(char)
    return common_char
