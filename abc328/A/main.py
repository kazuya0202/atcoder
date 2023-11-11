def main():
    n, m = map(int, input().split())
    list_ = list(map(int, input().split()))

    sum_ = 0
    for si in list_:
        if si <= m:
            sum_ += si

    print(sum_)


if __name__ == "__main__":
    main()
