def main():
    n, t = map(int, input().split())

    points = [0] * n
    for _ in range(t):
        a, b = map(int, input().split())
        points[a - 1] += b

        print(len(set(points)))


if __name__ == "__main__":
    main()
