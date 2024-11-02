def main():
    n = int(input())
    a_list = list(map(int, input().split()))

    b_list = []
    map_dict = {}

    for i in range(n):
        x = a_list[i]
        if x not in map_dict:
            b_list.append(-1)
        else:
            b_list.append(map_dict[x])
        map_dict[x] = i + 1

    print(" ".join(map(str, b_list)))


if __name__ == "__main__":
    main()
