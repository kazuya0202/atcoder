def main():
    n = int(input())
    a_list = list(map(int, input().split()))
    p_list = list(map(int, input().split()))

    # for _ in range(10**5):
    for _ in range(n):
        for i, p in enumerate(p_list):
            a_list[p - 1] += a_list[i + 1]

    a0 = a_list[0]
    if a0 > 0:
        print("+")
    elif a0 < 0:
        print("-")
    else:
        print("0")


if __name__ == "__main__":
    main()
