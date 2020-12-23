with open("input5.txt") as f:
    print(max([int("".join(["0" if c == "F" or c == "L" else "1" for c in line]), 2) for line in f.read().splitlines()]))

