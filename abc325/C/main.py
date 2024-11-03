import itertools
from collections import deque

dx = [1, 0, -1, 0, 1, 1, -1, -1]
dy = [0, 1, 0, -1, 1, -1, 1, -1]


def main():
    h, w = map(int, input().split())
    S = []
    for _ in range(h):
        S.append([c for c in input()])

    id_ = 0
    connected = [[-1] * w for _ in range(h)]

    queue = deque()

    for i, j in itertools.product(range(h), range(w)):
        if S[i][j] == "#" and connected[i][j] == -1:
            queue.append((i, j))

            while queue:
                x, y = queue.popleft()
                for di, dj in zip(dx, dy):
                    nx = x + di
                    ny = y + dj
                    if (
                        0 <= nx < h
                        and 0 <= ny < w
                        and S[nx][ny] == "#"
                        and connected[nx][ny] == -1
                    ):
                        connected[nx][ny] = id_
                        queue.append((nx, ny))
            id_ += 1

    print(id_)


if __name__ == "__main__":
    main()
