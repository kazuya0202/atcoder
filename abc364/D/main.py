import heapq


def main():
    n, q = map(int, input().split())
    a_list = list(map(int, input().split()))
    b_list = []
    k_list = []
    for _ in range(q):
        b, k = map(int, input().split())
        b_list.append(b)
        k_list.append(k)

    for b, k in zip(b_list, k_list):
        heap = []
        for a in a_list:
            heapq.heappush(heap, abs(a - b))

        for _ in range(k - 1):
            heapq.heappop(heap)

        print(heapq.heappop(heap))


if __name__ == "__main__":
    main()
