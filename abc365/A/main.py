def main():
    y = int(input())

    days = 365
    if y % 400 == 0:
        days = 366
    elif y % 100 == 0:
        days = 365
    elif y % 4 == 0:
        days = 366
    else:
        days = 365

    print(days)


if __name__ == "__main__":
    main()
