def read_magic_number(path: str) -> bool:
    try:
        with open(path, "r") as f:
            line = f.readline()
    except FileNotFoundError:
        raise ValueError
    try:
        if 3 > float(line) >= 1:
            return True
        else:
            return False
    except ValueError:
        return False
