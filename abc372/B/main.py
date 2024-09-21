def main():
    M = int(input())

    def find_comb(m, current_combination):
        if m == 0:
            print(len(current_combination))
            print(*current_combination)
            return True

        if m < 0:
            return False

        for i in range(10, -1, -1):
            if find_comb(m - 3**i, current_combination + [i]):
                return True
        return False

    find_comb(M, [])


if __name__ == "__main__":
    main()
