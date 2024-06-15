def main():
    n, a = map(int, input().split())
    t_list = list(map(int, input().split()))

    time_sum = 0
    for t in t_list:
        if t < time_sum:
            time_sum = time_sum + a
        else:
            time_sum = t + a
        print(time_sum)


if __name__ == "__main__":
    main()
