def main():
    n = int(input())

    cur_x = 0
    cur_y = 0
    dist = 0
    for _ in range(n):
        x, y = map(int, input().split())
        diff_x = cur_x - x
        diff_y = cur_y - y
        dist += (diff_x**2 + diff_y**2) ** 0.5

        cur_x = x
        cur_y = y

    diff_x = cur_x - 0
    diff_y = cur_y - 0
    dist += (diff_x**2 + diff_y**2) ** 0.5
    print(dist)


if __name__ == "__main__":
    main()
