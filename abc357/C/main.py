def process(grid, n, grid_size, grid_edge, start_i, start_j):
    if n == 0:
        return

    for i in range(grid_size):
        for j in range(grid_size):
            xi = start_i + i
            xj = start_j + j
            if (
                grid_edge - 1 < i < grid_size - grid_edge
                and grid_edge - 1 < j < grid_size - grid_edge
            ):
                grid[xi][xj] = "."

    for i in range(3):
        for j in range(3):
            process(
                grid,
                n - 1,
                grid_size // 3,
                grid_edge // 3,
                start_i + i * grid_edge,
                start_j + j * grid_edge,
            )


def main():
    n = int(input())

    grid_size = 3**n
    grid_edge = 3 ** (n - 1)

    grid = [["#"] * grid_size for _ in range(grid_size)]
    process(grid, n, grid_size, grid_edge, 0, 0)

    for i in range(grid_size):
        print("".join(grid[i]))


if __name__ == "__main__":
    main()
