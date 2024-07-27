def main():
    n, x, y = map(int, input().split())
    a_list = list(map(int, input().split()))
    b_list = list(map(int, input().split()))

    a_list.sort(reverse=True)
    b_list.sort(reverse=True)

    sum_a = 0
    sum_b = 0
    for i in range(n):
        sum_a += a_list[i]
        sum_b += b_list[i]

        if sum_a > x:
            print(i + 1)
            return
        if sum_b > y:
            print(i + 1)
            return

    print(n)


if __name__ == "__main__":
    main()
