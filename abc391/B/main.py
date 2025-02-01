from itertools import product


def check_grid(S: list[str], T: list[str], i: int, j: int) -> bool:
    for y, x in product(range(len(T)), range(len(T))):
        if S[i + y][j + x] != T[y][x]:
            return False
    return True


def main():
    n, m = map(int, input().split())
    S = [input() for _ in range(n)]
    T = [input() for _ in range(m)]

    for i, j in product(range(n - m + 1), range(n - m + 1)):
        if check_grid(S, T, i, j):
            print(i + 1, j + 1)
            return


if __name__ == "__main__":
    main()
