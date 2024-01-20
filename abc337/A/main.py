def main():
    n = int(input())
    a_sum = 0
    b_sum = 0
    for _ in range(n):
        a, b = map(int, input().split())
        a_sum += a
        b_sum += b

    if a_sum == b_sum:
        print("Draw")
    elif a_sum > b_sum:
        print("Takahashi")
    else:
        print("Aoki")


if __name__ == "__main__":
    main()
