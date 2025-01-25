def main():
    n = int(input())
    a_list = list(map(int, input().split()))

    combinations = set()
    combinations.add(tuple(a_list))
    for i in range(n):
        for j in range(i + 1, n):
            bag = a_list[i] + a_list[j]
            cp_a_list = a_list.copy()
            cp_a_list.remove(a_list[i])
            cp_a_list.remove(a_list[j])
            combinations.add((bag, *cp_a_list))

    print(combinations)

    x_set = set()
    for combination in combinations:
        x = 0
        for i in combination:
            x ^= i
        x_set.add(x)

    print(len(x_set))


if __name__ == "__main__":
    main()
