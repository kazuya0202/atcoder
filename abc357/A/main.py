def main():
    n, m = map(int, input().split())
    list_ = list(map(int, input().split()))

    cnt = 0
    for h in list_:
        m -= h
        if m >= 0:
            cnt += 1

    print(cnt)


if __name__ == "__main__":
    main()
