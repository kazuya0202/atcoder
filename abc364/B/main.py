def can_move(c, si, sj, xi) -> bool:
    if xi == "L":
        if sj - 1 < 0:
            return False
        return c[si][sj - 1] == "."
    elif xi == "R":
        if sj + 1 >= len(c[0]):
            return False
        return c[si][sj + 1] == "."
    elif xi == "U":
        if si - 1 < 0:
            return False
        return c[si - 1][sj] == "."
    elif xi == "D":
        if si + 1 >= len(c):
            return False
        return c[si + 1][sj] == "."

    return False


def main():
    h, w = map(int, input().split())
    si, sj = map(int, input().split())

    c = []
    for _ in range(h):
        c.append(list(input()))

    x = input()
    si -= 1
    sj -= 1

    for xi in x:
        if xi == "L":
            if sj - 1 >= 0 and c[si][sj - 1] == ".":
                sj -= 1
        elif xi == "R":
            if sj + 1 < len(c[0]) and c[si][sj + 1] == ".":
                sj += 1
        elif xi == "U":
            if si - 1 >= 0 and c[si - 1][sj] == ".":
                si -= 1
        elif xi == "D":
            if si + 1 < len(c) and c[si + 1][sj] == ".":
                si += 1

        # print(xi, si + 1, sj + 1)

    print(si + 1, sj + 1)


if __name__ == "__main__":
    main()
