def decimal_to_base(x, base):
    res = 0
    while x > 0:
        x = x // base
        if x != 0:
            res += 1
    return res


value = decimal_to_base(5, 2)
print(value)
