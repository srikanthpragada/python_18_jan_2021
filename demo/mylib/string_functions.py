def hasupper(st) -> bool:
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


print("In string_functions module")
