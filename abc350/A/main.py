def main():
    s = input()
    abc = s[:3]
    num = int(s[3:])

    if num != 316 and 0 < num < 350:
        print("Yes")
        return
    print("No")


if __name__ == "__main__":
    main()
