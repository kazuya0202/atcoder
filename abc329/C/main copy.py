# import sys

# sys.setrecursionlimit(100000)


# def recursive(s: str, kinds: set):
#     if len(s) < 1:
#         return
#     if s in kinds:
#         return

#     kinds.add(s)
#     # print(kinds)
#     recursive(s[1:], kinds)


# # def main():
# #     n = int(input())
# #     s = input()

# #     start_idx = 0
# #     char = s[0]
# #     kinds = set(char)

# #     i = 0
# #     while i < n:
# #         si = s[i]
# #         if char != si:
# #             str_ = s[start_idx:i]
# #             recursive(str_, kinds)

# #             char = si
# #             kinds.add(char)
# #             start_idx = i
# #         i += 1

# #     str_ = s[start_idx:]
# #     recursive(str_, kinds)

# #     if "" in kinds:
# #         kinds.remove("")
# #     print(len(kinds))


# # if __name__ == "__main__":
# #     main()


# from itertools import groupby


# def main():
#     n = int(input())
#     s = input()

#     kinds = set()

#     for char, group in groupby(s):
#         # print(char, list(group))
#         str_ = "".join(list(group))
#         recursive(str_, kinds)

#     print(len(kinds))


# if __name__ == "__main__":
#     main()

import sys
from itertools import groupby

sys.setrecursionlimit(100000)


def recursive(s: str, kinds: set):
    if len(s) < 1:
        return

    kinds.add(s)
    # print(kinds)
    recursive(s[1:], kinds)


def main():
    n = int(input())
    s = input()

    kinds = set()

    for char, group in groupby(s):
        # print(char, list(group))
        str_ = "".join(list(group))
        recursive(str_, kinds)

    print(len(kinds))


if __name__ == "__main__":
    main()
