def main():
    tmp = input().split()
    n = int(tmp[0])
    t = tmp[1]

    s = [""] * n
    for i in range(n):
        s[i] = input()

    list_ = []
    t_length = len(t)
    for i, si in enumerate(s):
        si_length = len(si)
        idx = i + 1

        # 一致
        if t == si:
            list_.append(idx)
            continue

        # 長さが2文字以上違う場合
        if abs(t_length - si_length) > 1:
            continue

        # 部分一致
        if si in t or t in si:
            list_.append(idx)
            continue

        # 長さは同じで1文字だけ違う場合
        is_marked = False
        if t_length == si_length:
            for j in range(t_length):
                if t[j] != si[j]:
                    if is_marked:
                        break
                    is_marked = True
            else:
                list_.append(idx)
            continue

        long_s = si
        short_s = t
        if t_length - len(long_s) > 0:
            long_s, short_s = short_s, long_s

        is_marked = False
        k = 0
        for j in range(len(long_s)):
            if long_s[j] != short_s[k]:
                if is_marked:
                    break
                is_marked = True
            else:
                k += 1
        else:
            list_.append(idx)

    if len(list_) == 0:
        print("0")
        return

    print(len(list_))
    list_ = map(str, list_)
    print(" ".join(list_))


if __name__ == "__main__":
    main()
