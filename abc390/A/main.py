def main():
    a_list = list(map(int, input().split()))

    for i in range(len(a_list) - 1):
        if a_list[i] != i + 1:
            a_list[i], a_list[i + 1] = a_list[i + 1], a_list[i]
            if a_list == sorted(a_list):
                print("Yes")
                return
            else:
                print("No")
                return
    print("No")


if __name__ == "__main__":
    main()
