import bisect


def main():
    n = int(input())
    ac_list = [(*map(int, input().split()), i) for i in range(n)]
    ans = set(range(1, n + 1))

    # sorted_by_a = sorted(ac_list, key=lambda x: x[0])
    sorted_by_c = sorted(ac_list, key=lambda x: x[1])

    for x in range(n):
        ac_x = ac_list[x]

        # cx < cy を満たす始まりの添え字を見つける
        idx = bisect.bisect_right(sorted_by_c, (ac_x[1],))
        # すでに捨てたものは無視
        if idx - 1 not in ans:
            continue
        # print(ac_x)
        # print(f"y={sorted_by_c[:idx - 1]}")

        # もともとの順序と比較
        for y in range(0, idx - 1):
            if ac_x[0] < sorted_by_c[y][0] and ac_x[2] < sorted_by_c[y][2]:
                # print(f"remove {xx[2] + 1}")
                ans.remove(ac_x[2] + 1)
                break

    # ac_list = sorted(ac_list, key=lambda x: x[0], reverse=True)
    # remove = set()
    # for x in range(n):
    #     for y in range(x + 1, n):
    #         ax, cx, i = ac_list[x]
    #         ay, cy, j = ac_list[y]

    #         if cx < cy:
    #             remove.add(j + 1)
    #         elif ay > ax and cy < cx:
    #             remove.add(i + 1)

    # ans = set(range(1, n + 1)) - remove
    print(len(ans))
    print(*sorted(ans))


if __name__ == "__main__":
    main()
