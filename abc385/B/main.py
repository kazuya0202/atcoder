def check_s(s_list, x, y):
    if 0 <= x < len(s_list) and 0 <= y < len(s_list[0]):
        if s_list[x][y] == "#":
            return False
        return True
    return False


def main():
    h, w, x, y = map(int, input().split())
    s_list = []
    for _ in range(h):
        s_list.append(list(input()))
    t = input()

    x -= 1
    y -= 1
    direction = {"L": (0, -1), "R": (0, 1), "U": (-1, 0), "D": (1, 0)}

    visited = set()
    for _t in list(t):
        dx, dy = direction[_t]
        if not check_s(s_list, x + dx, y + dy):
            continue
        x += dx
        y += dy

        if s_list[x][y] == "@":
            visited.add((x, y))

    print(x + 1, y + 1, len(visited))


if __name__ == "__main__":
    main()
