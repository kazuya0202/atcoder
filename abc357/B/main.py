def main():
    s = input()

    upper_letters = 0
    for c in s:
        if c.isupper():
            upper_letters += 1

    lower_letters = len(s) - upper_letters

    if upper_letters > lower_letters:
        s = s.upper()
    else:
        s = s.lower()
    print(s)


if __name__ == "__main__":
    main()
