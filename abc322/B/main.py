def main():
    n, m = map(int, input().split())
    s = input()
    t = input()

    is_prefix = t.startswith(s)
    is_postfix = t.endswith(s)
    if is_prefix and is_postfix:
        print("0")
    elif is_prefix:
        print("1")
    elif is_postfix:
        print("2")
    else:
        print("3")


if __name__ == "__main__":
    main()
