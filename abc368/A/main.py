from collections import deque


def main():
    n, k = map(int, input().split())
    a_list = list(map(int, input().split()))

    a_list = deque(a_list)
    for _ in range(k):
        a_list.appendleft(a_list.pop())

    print(" ".join(map(str, a_list)))


if __name__ == "__main__":
    main()
