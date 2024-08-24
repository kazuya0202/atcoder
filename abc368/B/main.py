def count_values(a_list):
    cnt = 0
    for a in a_list:
        if a > 0:
            cnt += 1
    return cnt


def main():
    n = int(input())
    a_list = list(map(int, input().split()))

    if count_values(a_list) <= 1:
        print(0)
        return

    times = 0
    while True:
        a_list.sort(reverse=True)
        a_list[0] = max(a_list[0] - 1, 0)
        a_list[1] = max(a_list[1] - 1, 0)

        if count_values(a_list) <= 1:
            break
        times += 1

    print(times + 1)


if __name__ == "__main__":
    main()
