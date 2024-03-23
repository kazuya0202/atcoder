import itertools
from collections import deque


def main():
    # 17回繰り返せば、b,wが100の場合長さ200の文字列になる => 20回繰り返せば十分
    S = "wbwbwwbwbwbw"
    w, b = map(int, input().split())

    S_inf = itertools.cycle(S)

    w_cnt = 0
    b_cnt = 0
    queue = deque()

    for _ in range(w + b):
        c = next(S_inf)
        queue.append(c)
        if c == "w":
            w_cnt += 1
        else:
            b_cnt += 1

    if w_cnt == w and b_cnt == b:
        print("Yes")
        return

    times = 0
    while times < 20:
        pop = queue.popleft()
        if pop == "w":
            w_cnt -= 1
        else:
            b_cnt -= 1

        c = next(S_inf)
        queue.append(c)
        if c == "w":
            w_cnt += 1
        else:
            b_cnt += 1

        if w_cnt == w and b_cnt == b:
            print("Yes")
            return
        times += 1

    print("No")


if __name__ == "__main__":
    main()
