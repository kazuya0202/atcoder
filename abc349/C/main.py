def main():
    s = input()
    t = input().lower()

    if t[-1] == "x":
        t = t[:-1]

    i = 0
    for c in t:
        while i < len(s) and s[i] != c:
            i += 1
        if i == len(s):
            print("No")
            return
        i += 1

    print("Yes")


if __name__ == "__main__":
    main()
