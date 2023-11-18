
import sys
from itertools import groupby

sys.setrecursionlimit(1 << 16)


cdef recursive(s: str):
    if len(s) < 1:
        return

    kinds.add(s)
    recursive(s[1:])


n = int(input())
s = input()

kinds = set()

for char, group in groupby(s):
    # print(char, list(group))
    str_ = "".join(list(group))

    if s in kinds:
        continue
    recursive(str_)

print(len(kinds))
