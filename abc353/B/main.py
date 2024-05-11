def main():
    n, k = map(int, input().split())
    a_list = list(map(int, input().split()))

    remain_seet = k
    cnt = 0
    for ai in a_list:
        if remain_seet >= ai:
            remain_seet -= ai
            continue

        remain_seet = k - ai
        cnt += 1

    if remain_seet != k:
        cnt += 1
    print(cnt)


if __name__ == "__main__":
    main()
