from itertools import groupby


def main():
    n = int(input())
    s = input()

    ascii_str = "abcdefghijklmnopqrstuvwxyz"
    kinds = {c: 0 for c in ascii_str}

    for c, group in groupby(s):
        length = len("".join(list(group)))  # joinしなくてもOK
        kinds[c] = max(kinds[c], length)

    print(sum(kinds.values()))


if __name__ == "__main__":
    main()
