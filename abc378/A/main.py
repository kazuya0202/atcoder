from itertools import groupby


def main():
    a_list = sorted(map(int, input().split()))
    group = groupby(a_list)
    ans = 0
    for key, value in group:
        ans += len(list(value)) // 2

    print(ans)


if __name__ == "__main__":
    main()
