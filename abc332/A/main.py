def main():
    n, s, k = map(int, input().split())

    # pq_list = []
    total_price = 0
    for i in range(n):
        p, q = map(int, input().split())
        total_price += p * q

    if total_price < s:
        print(total_price + k)
    else:
        print(total_price)


if __name__ == "__main__":
    main()
