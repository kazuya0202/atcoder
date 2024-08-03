def main():
    n = int(input())
    a_list = list(map(int, input().split()))

    pair = [(a, i + 1) for i, a in enumerate(a_list)]
    pair = sorted(pair, reverse=True, key=lambda x: x[0])

    print(pair[1][1])


if __name__ == "__main__":
    main()
