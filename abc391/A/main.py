def main():
    d = input()

    x = {
        "N": "S",
        "S": "N",
        "E": "W",
        "W": "E",
    }
    for c in list(d):
        if c in x:
            print(x[c], end="")
    print()


if __name__ == "__main__":
    main()
