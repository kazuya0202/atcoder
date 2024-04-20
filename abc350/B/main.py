def main():
    n, m = map(int, input().split())
    list_ = list(map(int, input().split()))

    teeth = set(range(1, n + 1))
    for x in list_:
        if x in teeth:
            teeth.remove(x)
        else:
            teeth.add(x)

    print(len(teeth))


if __name__ == "__main__":
    main()
