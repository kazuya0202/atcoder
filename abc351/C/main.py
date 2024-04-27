import sys

sys.setrecursionlimit(2000000)


def recursive(stack: list):
    if len(stack) <= 1:
        return

    if stack[-1] != stack[-2]:
        return
    else:
        x, _ = stack.pop(), stack.pop()
        stack.append(x + 1)

    return recursive(stack)


def main():
    n = int(input())
    list_ = list(map(int, input().split()))

    stack = []
    for i in range(n):
        stack.append(list_[i])

        recursive(stack)

    print(len(stack))


if __name__ == "__main__":
    main()
