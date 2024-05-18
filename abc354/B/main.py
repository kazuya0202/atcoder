def main():
    n = int(input())
    sc_map = {}

    for _ in range(n):
        s, c = input().split()
        sc_map[s] = int(c)

    sum_c = sum(sc_map.values())
    sorted_sc = sorted(sc_map.items(), key=lambda x: x[0])
    print(sorted_sc[sum_c % n][0])


if __name__ == "__main__":
    main()
