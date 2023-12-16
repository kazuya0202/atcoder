def main():
    s = input()
    t = input()

    s1, s2 = s[0], s[1]
    t1, t2 = t[0], t[1]

    matrix = {
        "A": [0, 1, 2, 2, 1],
        "B": [1, 0, 1, 2, 2],
        "C": [2, 1, 0, 1, 2],
        "D": [2, 2, 1, 0, 1],
        "E": [1, 2, 2, 1, 0],
    }

    s_len = matrix[s1][ord(s2) - 65]
    t_len = matrix[t1][ord(t2) - 65]

    if s_len == t_len:
        print("Yes")
    else:
        print("No")


if __name__ == "__main__":
    main()
