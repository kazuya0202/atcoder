def main():
    s = input()

    ans_set = set()
    for i in range(len(s)):
        string = s[i:]
        for j in range(1, len(string) + 1):
            ans_set.add(string[:j])

    print(len(ans_set))


if __name__ == "__main__":
    main()
