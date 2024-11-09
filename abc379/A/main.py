def main():
    n = int(input())
    a = n // 100
    b = n // 10 % 10
    c = n % 10

    print("".join(map(str, [b, c, a])), "".join(map(str, [c, a, b])))


if __name__ == "__main__":
    main()
