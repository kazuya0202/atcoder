def main():
    s = input()
    targets = ["a", "e", "i", "o", "u"]

    for target in targets:
        s = s.replace(target, "")

    print(s)


if __name__ == "__main__":
    main()
