def cannot_replace(c: str) -> bool:
    return c not in ["a", "t", "c", "o", "d", "e", "r", "@"]


def main():
    s = input()
    t = input()

    for a, b in zip(s, t):
        if a == "@":
            if cannot_replace(b):
                print("You will lose")
                return
        elif b == "@":
            if cannot_replace(a):
                print("You will lose")
                return
        elif a != b:
            print("You will lose")
            return

    print("You can win")


if __name__ == "__main__":
    main()
