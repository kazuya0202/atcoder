def main():
    board = []
    for _ in range(4):
        board.append(list(map(str, input().split())))

    for line in reversed(board):
        print(*reversed(line))


if __name__ == "__main__":
    main()
