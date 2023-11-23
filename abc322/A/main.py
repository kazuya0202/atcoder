def main():
    n = int(input())
    s = input()

    idx = s.find("ABC")
    if idx != -1:
        idx += 1
    print(idx)


if __name__ == "__main__":
    main()
