def main():
    n = int(input())
    h_list = list(map(int, input().split()))

    max_cnt = 1
    for i in range(n):
        cur = h_list[i]
        for step in range(1, n - i):
            cnt = 0
            for j in range(i, n, step):
                if cur == h_list[j]:
                    cnt += 1
                else:
                    break
                max_cnt = max(max_cnt, cnt)

    print(max_cnt)


if __name__ == "__main__":
    main()
