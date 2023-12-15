def get_divisor(n: int) -> list:
    divisors = []
    for i in range(1, 10):  # 1-9
        if n % i == 0:
            divisors.append(i)
    return divisors


def main():
    n = int(input())
    divisors = get_divisor(n)

    x = []
    for i in range(n + 1):
        for d in divisors:
            if i % (n / d) == 0:
                x.append(d)
                break
        else:
            x.append("-")
    print("".join(map(str, x)))


if __name__ == "__main__":
    main()
