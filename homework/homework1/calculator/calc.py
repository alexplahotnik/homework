def check_power_of_2(a: int) -> bool:
    try:
        return not (bool(a & (a - 1)))
    except TypeError:
        return False
