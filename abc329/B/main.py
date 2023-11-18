def main():
    n = int(input())
    a_list = list(map(int, input().split()))

    values = sorted(set(a_list))
    print(values[-2])


if __name__ == "__main__":
    main()
