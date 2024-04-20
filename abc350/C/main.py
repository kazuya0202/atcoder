def main():
    n = int(input())
    list_ = list(map(int, input().split()))

    pair_dict = {x: i + 1 for i, x in enumerate(list_)}
    oppo_pair_dict = {v: k for k, v in pair_dict.items()}
    sorted_keys = sorted(pair_dict)
    pair_dict = {key: pair_dict[key] for key in sorted_keys}

    logs = []
    # print(pair_dict)
    for i in range(1, n + 1):
        idx = pair_dict[i]
        if idx != i:
            num = oppo_pair_dict[i]
            pair_dict[i] = i
            pair_dict[num] = idx
            oppo_pair_dict[i] = i
            oppo_pair_dict[idx] = num
            logs.append((i, idx))

    print(len(logs))
    for log in logs:
        print(log[0], log[1])


if __name__ == "__main__":
    main()
