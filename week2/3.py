def gcd_euclid(a, b):
    dividend = a if (a >= b) else b
    divisor = a if (a <= b) else b

    while divisor != 0:
        remainder = dividend % divisor
        dividend = divisor
        divisor = remainder

    return dividend
a, b = map(int, input().split())
print(gcd_euclid(a, b))