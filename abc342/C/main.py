def main():
    n = int(input())
    s = input()
    q = int(input())

    abc_str = "abcdefghijklmnopqrstuvwxyz"
    abc_str_change = "abcdefghijklmnopqrstuvwxyz"

    for _ in range(q):
        c, d = input().split()
        abc_str_change = abc_str_change.replace(c, d)

    dict_ = {a: b for a, b in zip(abc_str, abc_str_change)}
    for c in s:
        print(dict_[c], end="")
    print()


if __name__ == "__main__":
    main()
