from fractions import Fraction
from itertools import pairwise


def main():
    n = int(input())
    a_list = list(map(int, input().split()))

    coef = Fraction(a_list[1], a_list[0])
    for a, b in pairwise(a_list):
        if Fraction(b, a) != coef:
            print("No")
            return
    print("Yes")


if __name__ == "__main__":
    main()
