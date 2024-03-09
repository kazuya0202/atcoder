def main():
    n = int(input())
    a_set = set(map(int, input().split()))

    m = int(input())
    b_set = set(map(int, input().split()))

    l = int(input())
    c_set = set(map(int, input().split()))

    q = int(input())
    x_list = list(map(int, input().split()))

    sum_set = {a + b + c for a in a_set for b in b_set for c in c_set}

    for x in x_list:
        if x in sum_set:
            print("Yes")
        else:
            print("No")


if __name__ == "__main__":
    main()
