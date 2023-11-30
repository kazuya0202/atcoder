def main():
    k = int(input())

    if k <= 9:
        print(k)
        return

    digits = 1
    top_digit = 1
    cnt = 9
    i = 1
    # while cnt < k:
    for _ in range(10):
        digits += 1
        cnt += 2 * (10 - (digits - 1)) + 1
        for j in range(0, 10 - digits + 1):
            cnt += 2 * j + 1
        #     cnt += j * (digits - 1)
        print(cnt)

    print(cnt)


if __name__ == "__main__":
    main()
