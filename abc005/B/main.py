def main():
    n = int(input())
    t = [0] * n
    for i in range(n):
        t[i] = int(input())

    print(min(t))


if __name__ == "__main__":
    main()
