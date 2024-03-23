from itertools import pairwise


def main():
    n = int(input())
    list_ = list(map(int, input().split()))

    ans = [x * y for x, y in pairwise(list_)]
    print(" ".join(map(str, ans)))


if __name__ == "__main__":
    main()
