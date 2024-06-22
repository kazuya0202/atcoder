def main():
    n = int(input())
    list_ = list(map(int, input().split()))

    cnt = 0
    for i in range(1, len(list_) - 1):
        if list_[i - 1] == list_[i + 1]:
            cnt += 1
    print(cnt)


if __name__ == "__main__":
    main()
