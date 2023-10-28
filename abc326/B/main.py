def split(n):
    return n // 100, (n % 100) // 10, n % 10


def is_valid(a, b, c):
    return a * b == c


def main():
    n = int(input())

    if is_valid(*split(n)):
        print(n)
        return

    for i in range(n + 1, 919):
        if is_valid(*split(i)):
            print(i)
            return


if __name__ == "__main__":
    main()
