def main():
    MONTH, DAY = map(int, input().split())
    y, m, d = map(int, input().split())

    if m == MONTH and d == DAY:
        print(y + 1, 1, 1)
    elif d == DAY:
        print(y, m + 1, 1)
    else:
        print(y, m, d + 1)


if __name__ == "__main__":
    main()
