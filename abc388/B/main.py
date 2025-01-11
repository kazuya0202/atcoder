def main():
    n, d = map(int, input().split())
    snakes = []
    for _ in range(n):
        snakes.append(list(map(int, input().split())))

    for i in range(1, d + 1):
        max_weight = -1
        for t, l in snakes:
            max_weight = max(max_weight, t * (l + i))
        print(max_weight)


if __name__ == "__main__":
    main()
