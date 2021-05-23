def backspace_compare(first: str, second: str):
    """Compares two values, taking into account the backspace bar keystrokes"""
    result = []
    for elem in (first, second):
        for del_index in range(elem.count("#")):
            if not elem[0] == "#":
                elem = elem.replace(elem[elem.find("#", 1) - 1], "", 1)
            elem = elem.replace("#", "", 1)
        result.append(elem)
    if result[0] == result[1]:
        return True
    return False
