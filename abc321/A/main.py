from itertools import pairwise


def main():
    n = int(input())
    chars = list(map(int, str(n)))

    for a, b in pairwise(chars):
        if a <= b:
            print("No")
            return
    print("Yes")


if __name__ == "__main__":
    main()
