def main():
    n = int(input())
    A = []
    for _ in range(n):
        A.append([c for c in input()])

    for i in range(n // 2):
        i_ = n - i
        for x in range(i - 1, i_):
            xx = n - 1 - x
            for y in range(i - 1, i_):
                if xx < 0 or xx >= n:
                    print(xx)
                    continue
                [A[y][xx], A[x][y]] = [A[x][y], A[y][xx]]

    for a in A:
        print("".join(a))


if __name__ == "__main__":
    main()
