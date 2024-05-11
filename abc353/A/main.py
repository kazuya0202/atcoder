def main():
    n = int(input())
    h_list = list(map(int, input().split()))

    first_h = h_list[0]
    for i in range(1, n):
        if first_h < h_list[i]:
            print(i + 1)
            return

    print(-1)


if __name__ == "__main__":
    main()
