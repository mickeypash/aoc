# https://adventofcode.com/2022/day/1

def max_calories(expedition):
    # part 1
    return max([sum(x for x in i) for i in expedition])

def top_3_calories(expedition):
    #part 2
    return sum(sorted([sum(x for x in i) for i in expedition])[-3:])

if __name__ == '__main__':

    test = [
            [1000,2000,3000],
            [4000],
            [5000,6000],
            [7000,8000,9000],
            [10000]
    ]

    with open('input.txt', 'r') as file:
        lst = file.read().split('\n\n')
        lst = [[int(i) for i in x.splitlines()] for x in lst]

        print(top_3_calories(lst))

