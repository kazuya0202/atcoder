def main():
    a, b = map(int, input().split())
    ans = set()

    diff = b - a
    ans.add(a - diff)
    ans.add(b + diff)

    diff_half = diff // 2
    if a + diff_half == b - diff_half:
        ans.add(a + diff_half)

    print(len(ans))


if __name__ == "__main__":
    main()
