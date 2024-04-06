def main():
    n = int(input())
    ans = ["x" if i % 3 == 0 else "o" for i in range(1, n + 1)]

    print("".join(ans))


if __name__ == "__main__":
    main()
