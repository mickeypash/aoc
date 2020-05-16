"""
--- Day 1: Not Quite Lisp ---
https://adventofcode.com/2015/day/1
"""

def base(directions: str):
    UP = "("
    DOWN = ")"
    floor = 0
    for d in directions:
        if d == UP:
            floor += 1
        elif d == DOWN:
            floor -= 1
    return(floor)

def main(directions: str):
    return sum(map(lambda x: 1 if x == "(" else -1, [d for d in directions]))

if __name__ == '__main__':
    assert main("(())") == 0
    assert main("()()") == 0

    assert main("(((") == 3
    assert main("(()(()(") == 3
    assert main("))(((((") == 3

    assert main("())") == -1
    assert main("))(") == -1

    assert main(")))") == -3
    assert main(")())())") == -3
