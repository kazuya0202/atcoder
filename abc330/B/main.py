def main():
    n, l, r = map(int, input().split())
    list_ = list(map(int, input().split()))

    ans_list = []

    for ai in list_:
        if l >= ai:
            ans_list.append(l)
        elif l < ai < r:
            ans_list.append(ai)
        else:
            ans_list.append(r)
    print(" ".join(map(str, ans_list)))


if __name__ == "__main__":
    main()
