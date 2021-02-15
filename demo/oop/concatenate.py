def cat(st1, st2):
    if isinstance(st2,str):
        return st1 + st2
    else:
        return st1 + str(st2)


print(cat("abc", "xyz"))
print(cat("abc", 10))
