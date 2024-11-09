from collections import deque


def main():
    n, m = map(int, input().split())
    x_list = list(map(int, input().split()))
    a_list = list(map(int, input().split()))

    cells = [0] * n
    for i in range(m):
        cells[x_list[i] - 1] = a_list[i]

    queue = deque()
    moves = 0
    for i in range(n):
        if cells[i] == 0:
            if len(queue) == 0:
                print(-1)
                return
            elif len(queue) > 0:
                moves += i - queue.popleft()

        surplus = cells[i] - 1
        for _ in range(surplus):
            queue.append(i)

    if len(queue) > 0:
        print(-1)
    else:
        print(moves)


if __name__ == "__main__":
    main()
