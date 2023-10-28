def main():
    x, y = map(int, input().split())

    diff = x - y
    use_elevator = -2 <= diff <= 3
    if use_elevator:
        print("Yes")
    else:
        print("No")


if __name__ == "__main__":
    main()
