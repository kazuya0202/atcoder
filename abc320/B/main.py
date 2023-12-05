def get_length_palindrome(s: str, left: int, right: int):
    s_len = len(s)
    while left >= 0 and right < s_len and s[left] == s[right]:
        left -= 1
        right += 1

    return right - left - 1


def main():
    s = input()
    max_length = 1

    for i in range(len(s)):
        length = get_length_palindrome(s, i, i)
        max_length = max(max_length, length)
        length = get_length_palindrome(s, i, i + 1)
        max_length = max(max_length, length)

    print(max_length)


if __name__ == "__main__":
    main()
