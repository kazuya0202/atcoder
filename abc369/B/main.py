def main():
    n = int(input())
    a_list: list[int] = []
    s_list: list[str] = []

    for _ in range(n):
        a, s = input().split()
        a_list.append(int(a))
        s_list.append(s)

    left_hand = -1
    right_hand = -1
    cost = 0

    for i in range(n):
        if s_list[i] == "L":
            if left_hand == -1:
                left_hand = a_list[i]
                continue
            cost += abs(a_list[i] - left_hand)
            left_hand = a_list[i]
        elif s_list[i] == "R":
            if right_hand == -1:
                right_hand = a_list[i]
                continue
            cost += abs(a_list[i] - right_hand)
            right_hand = a_list[i]

    print(cost)


if __name__ == "__main__":
    main()
