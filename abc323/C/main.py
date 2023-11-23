from collections import namedtuple


def main():
    n, m = map(int, input().split())
    scores = list(map(int, input().split()))

    Player = namedtuple("Player", ["id", "score", "status", "more"])
    players: list[Player] = []

    top_player = Player(id=0, score=0, status="", more=0)
    for i in range(n):
        si = [c for c in input()]
        total_score = i + 1
        for status, score in zip(si, scores):
            if status == "o":
                total_score += score

        p = Player(id=i + 1, score=total_score, status=si, more=0)
        players.append(p)

        if total_score > top_player.score:
            top_player = p
        # print(p)

    # scores.sort(reverse=True)
    for i, p in enumerate(players):
        cur_score = p.score
        if cur_score >= top_player.score:
            continue
        cnt = 0

        sorted_pairs = sorted(zip(scores, p.status), reverse=True)
        tuples = zip(*sorted_pairs)
        sorted_scores, sorted_status = [list(tuple) for tuple in tuples]
        # print(sorted_scores, sorted_status)
        for status, score in zip(sorted_status, sorted_scores):
            if status == "x":
                cur_score += score
                cnt += 1
            if cur_score >= top_player.score:
                players[i] = Player(id=p.id, score=cur_score, status=p.status, more=cnt)
                break

    for p in players:
        print(p.more)


if __name__ == "__main__":
    main()
