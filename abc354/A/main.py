def main():
    h = int(input())

    plant_height = 0
    i = 0
    while h >= plant_height:
        plant_height += 2**i
        i += 1

    print(i)


if __name__ == "__main__":
    main()
