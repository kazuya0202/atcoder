import math


def main():
    n = int(input())  # ゴミの種類
    q_list = []
    r_list = []
    for _ in range(n):
        q, r = map(int, input().split())
        q_list.append(q)
        r_list.append(r)

    q = int(input())  # 質問の数
    t_list = []
    d_list = []
    for _ in range(q):
        t, d = map(int, input().split())
        t_list.append(t)
        d_list.append(d)

    for t, d in zip(t_list, d_list):
        q = q_list[t - 1]
        r = r_list[t - 1]

        if d < q and d <= r:
            ans = r
        else:
            ans = q * (d // q) + r
            if ans < d:
                ans += q

        print(ans)


if __name__ == "__main__":
    main()
