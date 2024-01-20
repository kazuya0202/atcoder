import itertools


def main():
    s = input()

    abc = "".join([k for k, g in itertools.groupby(s)])

    if abc in ["A", "B", "C", "AB", "AC", "BC", "ABC"]:
        print("Yes")
    else:
        print("No")


if __name__ == "__main__":
    main()
