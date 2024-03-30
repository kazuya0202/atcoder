def main():
    n, a, b = map(int, input().split())
    list_ = list(map(int, input().split()))

    if len(list_) == 1:
        print("Yes")
        return

    week_num = a + b

    norm_list = {x % week_num for x in list_}
    # 全て同じ曜日になった時
    if len(norm_list) == 1:
        print("Yes")
        return

    sorted_norm_list = sorted(norm_list)
    diff = sorted_norm_list[-1] - sorted_norm_list[0]
    diff2 = sorted_norm_list[-1] - sorted_norm_list[-2]

    # 全て週の前半 or 週末と週の始まりを跨ぐ場合
    if diff < a or diff2 >= week_num - (a - 1):
        print("Yes")
    else:
        print("No")


if __name__ == "__main__":
    main()
