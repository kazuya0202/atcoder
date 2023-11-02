from decimal import Decimal


def main():
    n = Decimal(int(input()))

    expected_value = Decimal(0)
    for i in range(1, int(n) + 1):
        expected_value += i / n
    print(int(expected_value * 10000))


if __name__ == "__main__":
    main()
