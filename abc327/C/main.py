def main():
    a = []
    for i in range(9):
        a.extend(map(int, input().split()))

    for i in range(9):
        # horizontal
        idx = i * 9
        x = set(a[idx : idx + 9])
        if len(x) != 9:
            print("No")
            return

        # vertical
        y = set(a[i::9])
        if len(y) != 9:
            print("No")
            return

    # 3x3
    start = 0
    for i in range(3):
        for j in range(3):
            idx = j * 3 + start
            z = set(
                [*a[idx : idx + 3], *a[idx + 9 : idx + 12], *a[idx + 18 : idx + 21]]
            )
            if len(z) != 9:
                print("No")
                return
        start += 27

    print("Yes")


if __name__ == "__main__":
    main()
