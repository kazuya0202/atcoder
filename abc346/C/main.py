def main():
    n, k = map(int, input().split())
    list_ = list(map(int, input().split()))

    sum_ = k * (k + 1) // 2
    for x in set(list_):
        if x <= k:
            sum_ -= x
    print(sum_)


if __name__ == "__main__":
    main()
