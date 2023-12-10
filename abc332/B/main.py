def main():
    k, g, m = map(int, input().split())

    glass = 0
    mugcup = m
    for _ in range(k - 1):
        if glass == g:
            glass = 0
        elif mugcup == 0:
            mugcup = m
        else:
            amount = min(mugcup, g - glass)
            mugcup -= amount
            glass += amount

    print(glass, mugcup)


if __name__ == "__main__":
    main()
