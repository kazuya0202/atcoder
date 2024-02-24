def main():
    s = input()
    c_list = [c for c in s]

    a = c_list[0]
    b = c_list[1]
    if a != b:
        if s.count(a) > s.count(b):
            print(2)
            exit()
        else:
            print(1)
            exit()

    prev = c_list[0]
    for i, c in enumerate(c_list):
        if prev != c:
            print(i + 1)
            exit()
        prev = c


if __name__ == "__main__":
    main()
