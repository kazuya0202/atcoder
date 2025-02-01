def main():
    n, q = map(int, input().split())
    queries = [list(map(int, input().split())) for _ in range(q)]

    birds = [i + 1 for i in range(n)]
    nests = [1 for _ in range(n)]

    over_ones = 0

    for q, *ph in queries:
        if q == 1:
            p, h = ph
            prev = birds[p - 1]
            nests[prev - 1] -= 1

            birds[p - 1] = h
            nests[h - 1] += 1

            if nests[prev - 1] == 1:
                over_ones -= 1
            if nests[h - 1] == 2:
                over_ones += 1
        elif q == 2:
            print(over_ones)


if __name__ == "__main__":
    main()
