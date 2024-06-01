def main():
    n, l, r = map(int, input().split())

    list_ = list(range(1, n + 1))
    mid = reversed(list_[l - 1 : r])
    start = list_[: l - 1]
    end = list_[r:]

    print(*start, *mid, *end)


if __name__ == "__main__":
    main()
