import itertools


def main():
    n = int(input())
    a_list = list(map(int, input().split()))

    for bits in itertools.product([0, 1], repeat=n):
        print(bits)


if __name__ == "__main__":
    main()
