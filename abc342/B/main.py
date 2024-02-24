def main():
    n = int(input())
    p_list = list(map(int, input().split()))
    q = int(input())

    persons = {p: idx for idx, p in enumerate(p_list)}

    for _ in range(q):
        a, b = map(int, input().split())
        if persons[a] < persons[b]:
            print(a)
        else:
            print(b)


if __name__ == "__main__":
    main()
