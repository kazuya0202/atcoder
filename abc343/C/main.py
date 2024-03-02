def is_palindrome(num: int):
    s = str(num)
    return s == s[::-1]


def main():
    n = int(input())

    palindromes = [1, 8]

    num_cubic = 3**3
    num = 3
    while num_cubic <= 1e18:
        num_cubic = num**3

        if is_palindrome(num_cubic):
            palindromes.append(num_cubic)
        num += 1

    for i, palindrome in enumerate(palindromes):
        if n < palindrome:
            print(palindromes[i - 1])
            return


if __name__ == "__main__":
    main()
