def main():
    w = input()
    list_ = []
    for char in w:
        if char not in ["a", "i", "u", "e", "o"]:
            list_.append(char)

    print("".join(list_))


if __name__ == "__main__":
    main()
