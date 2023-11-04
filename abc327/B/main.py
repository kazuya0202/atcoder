def main():
    b = int(input())

    # for i in range(1, math.ceil(math.sqrt(b))):
    # 10^18 をカバーできるまでの繰り返しで十分(15でもよさそう)
    for i in range(1, 16):
        if i**i == b:
            print(i)
            return

    print("-1")


if __name__ == "__main__":
    main()
