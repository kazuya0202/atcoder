def main():
    n = int(input())

    diff = -1
    sum_a = 0
    for _ in range(n):
        a, b = map(int, input().split())
        diff = max(diff, b - a)
        sum_a += a

    print(sum_a + diff)


if __name__ == "__main__":
    main()
