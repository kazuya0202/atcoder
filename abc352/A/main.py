def main():
    n, x, y, z = list(map(int, input().split()))

    min_, max_ = min(x, y), max(x, y)
    if z in range(min_, max_ + 1):
        print("Yes")
    else:
        print("No")


if __name__ == "__main__":
    main()
