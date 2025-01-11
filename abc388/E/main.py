import bisect


def main():
    n = int(input())
    a_list = list(map(int, input().split()))

    cnt = 0
    # while len(a_list) > 1:
    #     a = a_list.pop()
    #     half = a // 2
    #     idx = bisect.bisect_right(a_list, half) - 1
    #     if a_list[idx] > half:
    #         continue

    #     del a_list[idx]
    #     cnt += 1
    half = a_list.pop() // 2
    base_idx = bisect.bisect_right(a_list, half)

    for i in range(n, base_idx, -1):
        if len(a_list) < 2:
            break
        half = a_list.pop() // 2
        for j in range(base_idx, -1, -1):
            if a_list[j] > half:
                continue
            print(f"{i} -> {j}")
            base_idx = j - 1
            cnt += 1
            break
        # if a_list[base_idx] > half:
        #     continue

    print(cnt)


if __name__ == "__main__":
    main()
