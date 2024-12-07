from collections import deque


def main():
    h, w, d = map(int, input().split())
    grid = []

    queue = deque()
    INF = float("inf")
    visited = [[INF] * w for _ in range(h)]

    for i in range(h):
        row = list(input())
        grid.append(row)
        for j, cell in enumerate(row):
            if cell == "H":
                queue.append((i, j, 0))
                visited[i][j] = 0

    reachable_cells = set()
    directions = ((1, 0), (-1, 0), (0, 1), (0, -1))

    while queue:
        y, x, distance = queue.popleft()
        reachable_cells.add((y, x))

        if distance == d:
            continue

        for dy, dx in directions:
            ny, nx = y + dy, x + dx
            if (
                0 <= ny < h
                and 0 <= nx < w
                and grid[ny][nx] == "."
                and visited[ny][nx] > distance + 1
            ):
                visited[ny][nx] = distance + 1
                queue.append((ny, nx, distance + 1))

    print(len(reachable_cells))


if __name__ == "__main__":
    main()
