import bisect


def main():
    n = int(input())

    w = [0] * n
    x = [0] * n
    for i in range(n):
        w[i], x[i] = map(int, input().split())

    # sort by `x`
    wx = sorted(zip(x, w))
    x, w = zip(*wx)
    # print(x, w)

    max_ = 0
    for i, xi in enumerate(x):
        # 24は存在しないため、15まで（15+8 => 23）
        if 0 <= xi <= 15:
            idx = bisect.bisect_right(x, xi + 8)
            max_ = max(max_, sum(w[i:idx]))

        else:
            # xi = [22, 2, ...] みたいに分割される場合
            remain = 24 - xi
            left_side = bisect.bisect_right(x, 8 - remain)
            right_side = bisect.bisect_left(x, xi)
            # print(f"{left=}, {right=}")
            max_ = max(max_, sum(w[:left_side]) + sum(w[right_side:]))

    print(max_)


if __name__ == "__main__":
    main()
