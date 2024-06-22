def main() -> None:
    sx, sy = map(int, input().split())
    tx, ty = map(int, input().split())

    diff_x = abs(sx - tx)
    diff_y = abs(sy - ty)

    over_x = diff_x - diff_y
    x_cost = (diff_x - over_x) // 2

    if diff_x > 1:
        if diff_x % 2 == 1 and sx % 2 == 1:
            x_cost += 1
    if diff_y > 1:
        x_cost = max(0, x_cost - (diff_y - 1))

    if over_x > 0:
        x_cost += over_x // 2

    cost = x_cost + diff_y
    print(cost)


if __name__ == "__main__":
    main()
