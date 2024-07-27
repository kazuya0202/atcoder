def main():
    n = int(input())

    can_eat = True
    prev_sweet = False
    for _ in range(n):
        s = input()
        if not can_eat:
            print("No")
            return
        if s == "sweet":
            if prev_sweet:
                can_eat = False
            prev_sweet = True
        else:
            prev_sweet = False

    print("Yes")


if __name__ == "__main__":
    main()
