def main():
    n = int(input())
    ac_pairs = {}

    for _ in range(n):
        a, c = map(int, input().split())
        if c not in ac_pairs:
            ac_pairs[c] = a
        else:
            ac_pairs[c] = min(ac_pairs[c], a)

    print(max(ac_pairs.values()))


if __name__ == "__main__":
    main()
