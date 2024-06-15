def main():
    n, m = map(int, input().split())
    s_list = []
    for _ in range(n):
        x = input()
        x = x.replace("o", "1").replace("x", "0")
        s_list.append(int(x, 2))

    accessed = []
    max_bit_cnt = 0
    max_bit_cnt_at_same_cnt = float("inf")  # 同数の場合は被りが一番少ないものを探す

    # 最大のbit_countを探す
    for i in range(n):
        cnt = s_list[i].bit_count()
        if cnt > max_bit_cnt:
            max_bit_cnt = cnt
            accessed = [i]
        elif cnt == max_bit_cnt:
            lapped_bit_cnt = 0
            for j in range(n):
                if i == j:
                    continue
                lapped_bit_cnt += (s_list[i] & s_list[j]).bit_count()
            if lapped_bit_cnt < max_bit_cnt_at_same_cnt:
                max_bit_cnt_at_same_cnt = lapped_bit_cnt
                accessed = [i]
    if max_bit_cnt == m:
        print(len(accessed))
        return

    max_bit_cnt_at_same_cnt = float("inf")  # 同数の場合は被りが一番少ないものを探す
    base = s_list[accessed[0]]

    for i in range(n):
        max_idx = -1
        current_max = base

        for j in range(n):
            if j in accessed:
                continue
            union = base | s_list[j]
            if union > current_max:  # 今のループ内で最大になる場合
                max_idx = j
                current_max = union
            elif union == current_max:
                lapped_bit_cnt = 0
                # ? 等しいものだけをリストに残して、accessedに追加する際に、複数候補がある場合はその中から選ぶようにすればできるかも
                for k in range(n):
                    if k in accessed:
                        continue
                    lapped_bit_cnt += (s_list[j] & s_list[k]).bit_count()
                if lapped_bit_cnt < max_bit_cnt_at_same_cnt:
                    max_bit_cnt_at_same_cnt = lapped_bit_cnt
                    max_idx = j

        if max_idx != -1:
            base = union
            accessed.append(max_idx)
            # print(accessed)
        if union.bit_count() == m:
            print(len(accessed))
            return

    print(len(accessed))


if __name__ == "__main__":
    main()
