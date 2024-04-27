def main():
    a_list = list(map(int, input().split()))
    b_list = list(map(int, input().split()))

    score = sum(a_list) - sum(b_list) + 1
    print(score)


if __name__ == "__main__":
    main()
