from collections import namedtuple


def main():
    Point = namedtuple("Point", ["x1", "y1", "z1", "x2", "y2", "z2"])
    b1 = Point(*map(int, input().split()))
    b2 = Point(*map(int, input().split()))

    ok = [False, False, False]
    x_diff = min(b1.x2, b2.x2) - max(b1.x1, b2.x1)
    if x_diff > 0:
        ok[0] = True

    y_diff = min(b1.y2, b2.y2) - max(b1.y1, b2.y1)
    if y_diff > 0:
        ok[1] = True

    z_diff = min(b1.z2, b2.z2) - max(b1.z1, b2.z1)
    if z_diff > 0:
        ok[2] = True

    if all(ok):
        print("Yes")
    else:
        print("No")


if __name__ == "__main__":
    main()
