def main():
    n, m = map(int, input().split())
    a_list = list(map(int, input().split()))

    if sum(a_list) <= m:
        print("infinite")
        return

    for i in range(1, max(a_list) + 1):
        sum_ = 0
        for ai in a_list:
            sum_ += min(ai, i)
            if sum_ > m:
                print(i - 1)
                return


if __name__ == "__main__":
    main()
