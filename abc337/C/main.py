from dataclasses import dataclass
from typing import Optional


@dataclass
class Person:
    ai: int
    i: int
    next_: Optional["Person"] = None


def main():
    n = int(input())
    a_list = list(map(int, input().split()))

    persons: list[Person] = []
    for i, ai in enumerate(a_list):
        persons.append(Person(i=i + 1, ai=ai))

    start = persons[0]
    for p in persons:
        if p.ai == -1:
            start = p
        else:
            persons[p.ai - 1].next_ = p

    xs = [start.i]
    while start.next_:
        start = start.next_
        xs.append(start.i)
    print(" ".join([str(i) for i in xs]))


if __name__ == "__main__":
    main()
