a = 10
b = 20
a, b = b, a
print(a, b)

# while(b%=a) swap(a,b);
while b := b % a:
    b, a = a, b


def gcd(a, b):
    while b != 0:
        b = b % a
        b, a = a, b
    return a
