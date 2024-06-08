def main():
    n = int(input())
    MOD = 998244353

    dights = len(str(n))
    MOD_digits = len(str(MOD))
    times = (MOD_digits - dights) // dights
    times = min(times, n - 1)

    num = n
    for _ in range(times):
        num = num * 10 + n

    print(num % MOD)


if __name__ == "__main__":
    main()
