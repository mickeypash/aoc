# Day1 - https://adventofcode.com/2021/day/1

def load_input():
    with open('input1.txt', 'r') as file:
        for line in file:
            print(line.rstrip())

def solution(depths):
    previous = None
    for d in depths:
        if not previous:
            print(d, "N/A - no previous measurement")

if __name__ == '__main__':
    EXAMPLE = [
            199,
            200,
            208,
            210,
            200,
            207,
            240,
            269,
            260,
            263,
    ]

    solution(EXAMPLE)
