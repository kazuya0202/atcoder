def main():
    a, b = map(int, input().split())
    all_ = set(range(1, 4))

    ans = all_ - set([a, b])
    if len(ans) == 1:
        print(*ans)
    else:
        print(-1)


if __name__ == "__main__":
    main()
