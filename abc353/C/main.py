import itertools


def main():
    n = int(input())
    list_ = list(map(int, input().split()))

    sum_ = 0
    for a, b in itertools.combinations(list_, 2):
        x = a + b
        if x >= 1e8:
            sum_ += int(x % 1e8)
        else:
            sum_ += x

    print(sum_)


if __name__ == "__main__":
    main()
