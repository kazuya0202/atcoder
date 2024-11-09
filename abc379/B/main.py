def main():
    n, k = map(int, input().split())
    s = input()

    cnt = 0
    for x in s.split("X"):
        cnt += len(x) // k

    print(cnt)


if __name__ == "__main__":
    main()
