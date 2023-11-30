def main():
    n, x = map(int, input().split())
    score_list = list(map(int, input().split()))
    score_list.sort()

    # max を除外する値として考える場合
    left = score_list[:-1]
    left_diff = x - sum(left)
    if left_diff <= 0:
        # 合計が x 以上なら最小値=0
        print(0)
    else:
        # min を除外する値として考える場合
        right = score_list[1:]
        right_diff = x - sum(right)

        if right_diff <= 0:
            # 合計が x 以上なら最大値を小さくして x に合わせる (diff は負の値)
            print(score_list[-1] + right_diff)
        else:
            # 合計が x に満たない場合、-1 (自身が最大値になるため除外される)
            print(-1)


if __name__ == "__main__":
    main()
