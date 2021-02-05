def even_odd(numbers : list) -> tuple:
    odd = 0
    for n in numbers:
        if n % 2 == 1:
            odd += 1

    # No. of even numbers, no. of odd numbers
    return  (len(numbers) - odd, odd)



def hasupper(st : str) -> bool :
    for c in st:
        if c.isupper():
            return True

    return False


print( hasupper("abcDlksdjfklsf"))
print( even_odd( [10,11,5,6,9,21]))
