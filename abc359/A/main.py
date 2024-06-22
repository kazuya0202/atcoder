def main():
    n = int(input())
    cnt = 0
    for _ in range(n):
        input_str = input()
        if input_str == "Takahashi":
            cnt += 1

    print(cnt)


if __name__ == "__main__":
    main()
