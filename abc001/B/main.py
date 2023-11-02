def main():
    m = int(input())
    m /= 1000

    if m < 0.1:
        print("00")
    elif m <= 5:
        print(f"{int(m*10):02d}")
    elif m <= 30:
        print(int(m + 50))
    elif 35 <= m <= 70:
        print(int((m - 30) / 5 + 80))
    else:
        print("89")


if __name__ == "__main__":
    main()
