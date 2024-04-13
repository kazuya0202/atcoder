import itertools


def main():
    s = input()
    counter: dict[int, list[str]] = {}
    s = sorted(s)

    for k, v in itertools.groupby(s):
        length = len(list(v))
        if length not in counter:
            counter[length] = []
        counter[length].append(k)

    for k, v in counter.items():
        if len(v) not in [0, 2]:
            print("No")
            return

    print("Yes")


if __name__ == "__main__":
    main()
