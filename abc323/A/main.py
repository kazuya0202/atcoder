def main():
    s = input()

    even_s = s[1::2]
    if even_s == "0" * 8:
        print("Yes")
    else:
        print("No")


if __name__ == "__main__":
    main()
