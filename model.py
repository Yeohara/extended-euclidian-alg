def fast_power(a, b, n):
    if n == 1 and a != 0:
        return 0
    if a == 0:
        return 0
    if b == 0:
        return 1
    a = a % n
    res = 1
    while (b > 0):
        if ((b & 1) == 1):
            res = (res * a) % n
        b = b >> 1
        a = (a * a) % n
    return res

def eea(a, b):
    if a == 0:
        return (b, 0, 1)
    else:
        gcd, x, y = eea(b % a, a)
        return gcd, y - (b // a) * x, x

if __name__ == '__main__':
    a = 3242
    b = 34
    n = 234
    print(pow(a, b, n))
    print(fast_power(a, b, n))

    a = 1
    b = 1
    print (eea(a, b))
