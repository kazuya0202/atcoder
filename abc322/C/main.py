def main():
    n, m = map(int, input().split())
    firework_days = list(map(int, input().split()))

    cnt = 0

    for i in range(1, n + 1):
        day = firework_days[cnt]
        if i < day:
            print(day - i)
        elif i == day:
            print("0")
            cnt += 1


if __name__ == "__main__":
    main()
