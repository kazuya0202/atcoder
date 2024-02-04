def main():
    n = int(input())
    list_ = list(map(int, input().split()))

    current = 0
    sum_ = current
    for i in list_:
        sum_ += i
        if sum_ < 0:
            current += -sum_
            sum_ = 0

    print(sum_)


if __name__ == "__main__":
    main()
