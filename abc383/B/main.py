from itertools import combinations


def manhattan_distance(x1: int, y1: int, x2: int, y2: int) -> int:
    return abs(x1 - x2) + abs(y1 - y2)


def main():
    h, w, d = map(int, input().split())
    grid = []
    for i in range(h):
        grid.append(list(input()))
    reachable_cells = []

    for i in range(h):
        for j in range(w):
            if grid[i][j] != ".":
                continue

            cells = []
            for x in range(h):
                for y in range(w):
                    if grid[x][y] == "." and manhattan_distance(i, j, x, y) <= d:
                        cells.append((x, y))
            reachable_cells.append(cells)

    max_count = 0
    for comb in combinations(reachable_cells, 2):
        count = len(set(comb[0] + comb[1]))
        max_count = max(max_count, count)

    print(max_count)


if __name__ == "__main__":
    main()
