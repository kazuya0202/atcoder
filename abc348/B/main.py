import math


def main():
    n = int(input())
    xy_coords = []
    for _ in range(n):
        x, y = map(int, input().split())
        xy_coords.append((x, y))

    for i in range(n):
        max_distance = -1
        max_distance_idx = -1
        x1, y1 = xy_coords[i]
        for j in range(n):
            if i == j:
                continue

            x2, y2 = xy_coords[j]
            x = math.sqrt((x1 - x2) ** 2 + (y1 - y2) ** 2)
            if x > max_distance:
                max_distance = x
                max_distance_idx = j
        print(max_distance_idx + 1)


if __name__ == "__main__":
    main()
