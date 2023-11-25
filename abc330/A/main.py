def main():
    n, l = map(int, input().split())
    score_list = list(map(int, input().split()))

    cnt = 0
    for score in score_list:
        if score >= l:
            cnt += 1

    print(cnt)


if __name__ == "__main__":
    main()
