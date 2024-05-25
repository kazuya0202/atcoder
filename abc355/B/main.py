import itertools


def main():
    n, m = map(int, input().split())
    a_list = list(map(int, input().split()))
    b_list = list(map(int, input().split()))

    c_list = a_list + b_list
    c_list.sort()

    a_set = set(a_list)

    for x, y in itertools.pairwise(c_list):
        if x in a_set and y in a_set:
            print("Yes")
            return

    print("No")


if __name__ == "__main__":
    main()
