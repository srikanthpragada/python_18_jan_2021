def hasupper(st) -> bool:
    """
    Returns true if the given string has an uppercase letter, otherwise false.
    Parameter st is the string to be tested
    """
    for c in st:
        if c.isupper():
            return True

    return False


def countdigits(st) -> int:
    count = 0
    for c in st:
        if c.isdigit():
            count += 1

    return count


if __name__ == '__main__':
    print("Running string_functions module")
else:
    print("Importing string_functions module")
