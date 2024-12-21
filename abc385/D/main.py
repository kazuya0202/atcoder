def main():
    n, m, sx, sy = map(int, input().split())

    house_pos = set()
    for _ in range(n):
        house_pos.add(tuple(map(int, input().split())))

    direction = {"L": (-1, 0), "R": (1, 0), "U": (0, 1), "D": (0, -1)}

    visited = set()
    for _ in range(m):
        d, c = input().split()
        c = int(c)

        dx, dy = direction[d]
        new_sx = sx + dx * c
        new_sy = sy + dy * c

        for x, y in house_pos:
            if sx <= x <= new_sx and sy <= y <= new_sy:
                visited.add((x, y))
        house_pos -= visited

        sx = new_sx
        sy = new_sy

    print(sx, sy, len(visited))


if __name__ == "__main__":
    main()
