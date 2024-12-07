from math import sqrt


def factorization(n: int) -> set[int]:
    factors = set()
    if n < 1:
        return {-1}
    elif not isinstance(n, int):
        return {-1}
    elif n == 1:
        return {1}

    n1 = n
    for i in range(2, int(sqrt(n)) + 1):
        if n1 % i == 0:
            while n1 % i == 0:
                n1 //= i
                factors.add(i)
                if n1 == 1:
                    return factors
    if n1 != 1:
        factors.add(n1)
        return factors
    if not factors:
        return {n}
    return factors


def main():
    n = int(input())

    factors = factorization(n)


if __name__ == "__main__":
    main()
