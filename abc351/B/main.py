def main():
    n = int(input())
    a = ["".join([c for c in input()]) for _ in range(n)]
    b = ["".join([c for c in input()]) for _ in range(n)]

    for i in range(n):
        for row, (ai, bi) in enumerate(zip(a[i], b[i])):
            if ai != bi:
                print(i + 1, row + 1)
                return


if __name__ == "__main__":
    main()
