def decimal_to_base(x, base):
    res = ""
    while x > 0:
        res = str(x % base) + res
        x = x // base
    return res


value = decimal_to_base(10996, 16)
print(value)