def main():
    a, b, c = map(int, input().split())

    if a == b == c:
        print("Yes")
    elif a + b == c or b + c == a or c + a == b:
        print("Yes")
    else:
        print("No")


if __name__ == "__main__":
    main()
