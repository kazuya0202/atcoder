def main():
    n = int(input())

    ans_list = []
    for _ in range(n):
        row = map(int, input().split())
        ans = []
        for i, item in enumerate(row):
            if item == 1:
                ans.append(i + 1)
        ans_list.append(ans)

    all_empty = True
    for ans in ans_list:
        if len(ans) > 0:
            all_empty = False
            print(*ans)

    if all_empty:
        print()


if __name__ == "__main__":
    main()
