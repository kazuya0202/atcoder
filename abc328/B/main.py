def main():
    n = int(input())
    list_ = list(map(int, input().split()))

    cnt = 0
    for month, days in zip(range(1, n + 1), list_):
        if month >= 10:
            if month % 11 != 0:
                continue
            elif month % 10 <= days:
                cnt += 1

        if month <= days:
            cnt += 1
        if month * 11 <= days:
            cnt += 1

    print(cnt)


if __name__ == "__main__":
    main()
