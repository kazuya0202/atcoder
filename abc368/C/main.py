def main():
    n = int(input())
    h_list = list(map(int, input().split()))

    t = 0
    h_idx = 0
    while h_idx != n:
        hp = h_list[h_idx]
        remain = 3 - (t % 3)
        if hp <= remain:
            t += hp
            h_idx += 1
        else:
            a, b = divmod(h_list[h_idx], 5)
            t += a * 3
            if b <= 2:
                t += b
            else:
                t += 3
            h_idx += 1

    print(t)


if __name__ == "__main__":
    main()
