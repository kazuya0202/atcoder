def main():
    n, k = map(int, input().split())
    list_ = list(map(int, input().split()))

    ans = []
    for x in list_:
        if x % k == 0:
            ans.append(x // k)

    print(" ".join(map(str, ans)))


if __name__ == "__main__":
    main()
