from dataclasses import dataclass
# https://adventofcode.com/2022/day/2


# create an enum or mapping

# Rock     A X 1
# Paper    B Y 2
# Scissors C Z 3

# B > A
# C > B
# A > C


@dataclass
class Rock:
    letter: str = "A"
    score: int = 1

    def __eq__(self, other):
        return self.letter == other.letter

    def __lt__(self, other):
        return other.letter == "B"

    def __gt__(self, other):
        return other.letter == "C"

@dataclass
class Paper:
    letter: str = "B"
    score: int = 2

    def __eq__(self, other):
        return self.letter == other.letter

    def __lt__(self, other):
        return other.letter == "C"

    def __gt__(self, other):
        return other.letter == "A"

@dataclass
class Scissors:
    letter: str = "C"
    score: int = 3

    def __eq__(self, other):
        return self.letter == other.letter

    def __lt__(self, other):
        return other.letter == "A"

    def __gt__(self, other):
        return other.letter == "B"



def part1(lst):

    shape = {
            "A": Rock(),  # ROCK
            "B": Paper(),  # PAPER
            "C": Scissors(),  # SCISSORS
            "X": Rock(),
            "Y": Paper(),
            "Z": Scissors(),
    }

    total_score = []

    for r in lst:
        opp, me = r

        opp = shape[opp]
        me = shape[me]

        if me > opp:     # win
            total_score.append(me.score + 6)
        elif me == opp:  # draw
            total_score.append(me.score + 3)
        elif me < opp:   # loss
            total_score.append(me.score + 0)

    return sum(total_score)


def part2(lst):
    shape = {
            "A": Rock(),      # ROCK
            "B": Paper(),     # PAPER
            "C": Scissors(),  # SCISSORS
    }

    outcome = {
            "X": 0, # lose
            "Y": 3, # draw
            "Z": 6, # win
    }

    total_score = []

    for r in lst:
        opp, out = r

        opp = shape[opp]

        if out == "X": # lose
            if isinstance(opp, Rock):
                total_score.append(Scissors().score + outcome[out])
            elif isinstance(opp, Paper):
                total_score.append(Rock().score + outcome[out])
            elif isinstance(opp, Scissors):
                total_score.append(Paper().score + outcome[out])
        elif out == "Y": # draw
            total_score.append(opp.score + outcome[out])
        elif out == "Z": # win
            if isinstance(opp, Rock):
                total_score.append(Paper().score + outcome[out])
            elif isinstance(opp, Paper):
                total_score.append(Scissors().score + outcome[out])
            elif isinstance(opp, Scissors):
                total_score.append(Rock().score + outcome[out])

    return sum(total_score)

if __name__ == "__main__":
    test = [
            ("A", "Y"),
            ("B", "X"),
            ("C", "Z")
    ]
    print(part2(test))

    with open("input2.txt", "r") as f:
        lst = f.read().splitlines()
        lst = [l.split() for l in lst]

        print(part2(lst))

