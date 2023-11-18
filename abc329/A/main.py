def main():
    s = input()
    for c in s[:-1]:
        print(f"{c} ", end="")
    print(s[-1])


if __name__ == "__main__":
    main()
