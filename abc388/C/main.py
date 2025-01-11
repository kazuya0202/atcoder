import bisect


def main():
    n = int(input())
    a_list = list(map(int, input().split()))

    cnt = 0
    for a in a_list:
        cnt += max(bisect.bisect_right(a_list, a // 2), 0)
    print(cnt)


if __name__ == "__main__":
    main()
