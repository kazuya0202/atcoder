def main():
    n = int(input())
    t_list = []
    v_list = []

    for i in range(n):
        t, v = map(int, input().split())
        t_list.append(t)
        v_list.append(v)

    amount = 0
    prev_t = 0
    for t, v in zip(t_list, v_list):
        amount = max(0, amount - (t - prev_t))
        amount += v
        prev_t = t
    print(amount)


if __name__ == "__main__":
    main()
