from collections import namedtuple


def main():
    n = int(input())
    # s_list = []
    Player = namedtuple("Player", ["id", "win_count"])
    players: list[Player] = []

    for i in range(n):
        si = input()

        p = Player(id=i + 1, win_count=si.count("o"))
        players.append(p)

    players.sort(key=lambda x: x.win_count, reverse=True)
    print(" ".join([str(p.id) for p in players]))


if __name__ == "__main__":
    main()
