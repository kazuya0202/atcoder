from collections import deque
from itertools import product


def is_rectangle(area):
    x_list = []
    y_list = []
    for y, x in area:
        x_list.append(x)
        y_list.append(y)
    min_x = min(x_list)
    max_x = max(x_list)
    min_y = min(y_list)
    max_y = max(y_list)

    for y in range(min_y, max_y + 1):
        for x in range(min_x, max_x + 1):
            if (y, x) not in area:
                return False

    return True


def main():
    h, w = map(int, input().split())
    grid = [input() for _ in range(h)]

    visited = [[False] * w for _ in range(h)]
    connected_areas = []

    for y, x in product(range(h), range(w)):
        if grid[y][x] != "." and not visited[y][x]:
            area = []
            queue = deque([(y, x)])
            visited[y][x] = True
            area.append((y, x))

            while queue:
                cy, cx = queue.popleft()

                for dy, dx in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
                    ny = cy + dy
                    nx = cx + dx
                    if (
                        0 <= ny < h
                        and 0 <= nx < w
                        and not visited[ny][nx]
                        and grid[ny][nx] != "."
                    ):
                        visited[ny][nx] = True
                        queue.append((ny, nx))
                        area.append((ny, nx))
            connected_areas.append(area)

    is_rectangles = True
    for area in connected_areas:
        if not area:
            continue
        if not is_rectangle(area):
            is_rectangles = False
            break

    if is_rectangles:
        print("Yes")
    else:
        print("No")


if __name__ == "__main__":
    main()
