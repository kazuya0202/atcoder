def main():
    n, s, m, l = map(int, input().split())
    min_cost = float("inf")

    for s_cnt in range((n // 6) + 2):
        for m_cnt in range((n // 8) + 2):
            for l_cnt in range((n // 12) + 2):
                total_eggs = (s_cnt * 6) + (m_cnt * 8) + (l_cnt * 12)
                if total_eggs >= n:
                    total_cost = s_cnt * s + m_cnt * m + l_cnt * l
                    min_cost = min(min_cost, total_cost)

    print(min_cost)


if __name__ == "__main__":
    main()
