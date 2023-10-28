import sys

input = sys.stdin.readline

n, m = map(int, input().split())
ai_list = list(map(int, input().split()))

max_num = 0
ai_list = sorted(ai_list)
for i, x in enumerate(ai_list):
    cnt = 0
    for ai in ai_list[i:]:
        if x <= ai < x + m:
            cnt += 1
        else:
            break
    max_num = max(max_num, cnt)

print(max_num)
