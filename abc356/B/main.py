def main():
    n, m = map(int, input().split())
    a_list = list(map(int, input().split()))

    total_list = [0] * m
    for i in range(n):
        x_list = list(map(int, input().split()))
        for j, x in enumerate(x_list):
            total_list[j] += x

    for i in range(m):
        if total_list[i] < a_list[i]:
            print("No")
            return
    print("Yes")


if __name__ == "__main__":
    main()
