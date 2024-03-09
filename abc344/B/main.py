def main():
    a_list: list[int] = []
    while True:
        a = int(input())
        a_list.append(a)
        if a == 0:
            break

    reversed_a_list = a_list[::-1]
    for a in reversed_a_list:
        print(a)


if __name__ == "__main__":
    main()
