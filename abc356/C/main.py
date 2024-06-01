def main():
    n, m, k = map(int, input().split())

    testcases = {}
    for i in range(m):
        c, *keys, is_opened = input().split()
        c = int(c)
        keys = list(map(int, keys))

        testcases[is_opened] = {}


if __name__ == "__main__":
    main()
