def main():
    a, b = map(int, input().split())
    numbers = range(10)

    for n in numbers:
        if a + b != n:
            print(n)
            return


if __name__ == "__main__":
    main()
