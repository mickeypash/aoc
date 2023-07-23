# https://adventofcode.com/2022/day/3 


def rummage(rucksack):
    chunk = len(rucksack)//2
    comp1, comp2 = rucksack[:chunk], rucksack[chunk:]
    item = [i for i in comp1 if i in comp2].pop()
    return item


def chunks(lst, n=3):
    return [lst[i:i + n] for i in range(0, len(lst), n)]


def check_three_elves(rucksacks):
    rucksacks = [set(r) for r in rucksacks]
    item = set.intersection(*rucksacks)
    return "".join(item)


if __name__ == "__main__":

    lst = open("input3.txt").read().splitlines()

    letters = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
    priorities = {letter: i for i, letter in enumerate(letters, start=1)}

    test = [
        "vJrwpWtwJgWrhcsFMMfFFhFp",
        "jqHRNqRjqzjGDLGLrsFMfFZSrLrFZsSL",
        "PmmdzqPrVvPwwTWBwg",
        "wMqvLMZHhHMvwLHjbvcjnnSBnvTQFn",
        "ttgJtRGJQctTZtZT",
        "CrZsJsPPZsGzwwsLwLmpwMDw",
    ]

    # part 1
    print(sum([priorities[rummage(rucksack)] for rucksack in lst]))
    # part 2
    print(sum([priorities[check_three_elves(c)] for c in chunks(lst)]))
