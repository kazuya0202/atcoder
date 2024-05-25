def main():
    n, t = map(int, input().split())
    list_ = list(map(int, input().split()))

    rows = [0] * n
    cols = [0] * n
    diag1 = 0
    diag2 = 0

    for turn, num in enumerate(list_):
        x = (num - 1) // n
        y = (num - 1) % n

        rows[x] += 1
        cols[y] += 1

        # 対角線
        if x == y:
            diag1 += 1
        if x == n - 1 - y:
            diag2 += 1

        if rows[x] == n or cols[y] == n or diag1 == n or diag2 == n:
            print(turn + 1)
            return

    print(-1)


if __name__ == "__main__":
    main()
