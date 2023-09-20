import math

def factor_finder() -> list:
    number = int(input("Number: "))

    factors = []

    for i in range(2, int(math.sqrt(number)) + 1):
        if number % i == 0:
            factors.append(i)
            factors.append(int(number / i))

    factors.sort()
    return factors

print(*factor_finder())