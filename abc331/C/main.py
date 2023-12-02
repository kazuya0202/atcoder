def main():
    n = int(input())
    ai_list = list(map(int, input().split()))

    sorted_pairs = sorted(((ai, i) for i, ai in enumerate(ai_list)), reverse=True)
    result = [0] * n

    prev_val = sorted_pairs[0][0]  # 最大値をセット
    prev_sum = 0
    same_val_sum = 0

    for ai, i in sorted_pairs:
        if ai != prev_val:
            prev_val = ai
            prev_sum += same_val_sum
            same_val_sum = 0

        same_val_sum += ai
        result[i] = prev_sum

    print(" ".join(map(str, result)))


if __name__ == "__main__":
    main()
