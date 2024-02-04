def display(matrix: list):
    for val in matrix:
        print("".join(["." if i == -1 else "#" for i in val]))


def main():
    h, w, n = map(int, input().split())

    # -1: "."
    #  1: "#"
    matrix = [[-1] * w for _ in range(h)]

    times = 0
    i = 0
    j = 0

    degrees_pair = {
        -1: {0: (1, 0), 90: (0, -1), 180: (-1, 0), 270: (0, 1)},
        1: {0: (-1, 0), 90: (0, 1), 180: (1, 0), 270: (0, -1)},
    }

    degree = 270

    while times < n:
        current_pos = matrix[i][j]
        matrix[i][j] *= -1

        movement = degrees_pair[current_pos][degree]
        i += movement[0]
        j += movement[1]
        if i == -1:
            i = h - 1
        if j == -1:
            j = w - 1
        i %= h
        j %= w
        degree = (degree + (90 * -current_pos)) % 360

        times += 1
        # display(matrix)
    display(matrix)


if __name__ == "__main__":
    main()
