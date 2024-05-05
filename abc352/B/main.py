def main():
    s = input()
    t = input()

    i = 0
    j = 0
    ans_list = []
    while i < len(s):
        if s[i] == t[j]:
            i += 1
            j += 1
            ans_list.append(j)
        else:
            j += 1
    print(" ".join(map(str, ans_list)))


if __name__ == "__main__":
    main()
