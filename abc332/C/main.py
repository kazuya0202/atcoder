def calc_buy_cnt(cnt_dict: dict[str, int], have_t_shirt_cnt: int) -> int:
    if cnt_dict["either"] > have_t_shirt_cnt:
        cnt_dict["either"] -= have_t_shirt_cnt
    buy_cnt = max(0, cnt_dict["logo"] - cnt_dict["either"])
    return buy_cnt


def main():
    n, m = map(int, input().split())
    s = input()

    cnt_dict = {
        "logo": 0,
        "either": 0,
        "buy": 0,
    }

    for c in s:
        if c == "0":
            store_buy_cnt = cnt_dict["buy"]
            cnt_dict["buy"] += calc_buy_cnt(cnt_dict, m)
            cnt_dict["logo"] = -(cnt_dict["logo"] + store_buy_cnt)
            cnt_dict["either"] = 0
        elif c == "1":
            cnt_dict["either"] += 1
            cnt_dict["logo"] += 1
        elif c == "2":
            cnt_dict["logo"] += 1
        # print(cnt_dict)

    cnt_dict["buy"] += calc_buy_cnt(cnt_dict, m)
    print(cnt_dict["buy"])


if __name__ == "__main__":
    main()
