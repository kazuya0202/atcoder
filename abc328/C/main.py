import re


def main():
    n, q = map(int, input().split())
    s = input()
    # list_ = []
    list_ = [map(int, input().split()) for _ in range(q)]

    pat = re.compile(r"(?=(.)\1)")
    for l, r in list_:
        cnt = len(re.findall(pat, s[l - 1 : r]))
        print(cnt)


if __name__ == "__main__":
    main()
