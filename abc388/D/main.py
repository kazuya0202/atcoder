def main():
    n = int(input())
    a_list = list(map(int, input().split()))

    x = 0
    for i in range(n):
        d = a_list[i] - (n - i - 1) + max(0, -x)
        a_list[i] = max(0, d)
        x = d
        # if d < 0:
        #     print(f"{i+1} -> {d}")
        # for j in range(0, i):
        #     if a_list[j] > 0:
        #         a_list[j] -= 1
        #         a_list[i] += 1

    print(" ".join(map(str, a_list)))


if __name__ == "__main__":
    main()
