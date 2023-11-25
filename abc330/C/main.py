import math


def main():
    d = int(input())

    for i in range(math.isqrt(d)):
        value = d - i
        isqrt_value = math.isqrt(value)
        for j in range(isqrt_value):
            for k in range(isqrt_value):
                if j * j + k * k == value:
                    print(i)
                    return
        # if
        # x = math.isqrt(value)
        # y = math.sqrt(value - x)
        # # print(x, y)
        # print(f"{x=}, {math.sqrt(value-x)=}, {math.isqrt(value-x)=}")
        # if int(y) == y:
        #     print(i)
        #     break


if __name__ == "__main__":
    main()
