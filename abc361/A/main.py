def main():
    n, k, x = map(int, input().split())
    list_ = list(map(int, input().split()))

    list_.insert(k, x)
    print(" ".join(map(str, list_)))


if __name__ == "__main__":
    main()
