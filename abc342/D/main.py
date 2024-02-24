import math
from itertools import combinations


def main():
    n = int(input())
    a_list = list(map(int, input().split()))

    count = 0
    for a, b in combinations(a_list, 2):
        if math.sqrt(a * b) % 1 == 0:
            count += 1
    print(count)


if __name__ == "__main__":
    main()
