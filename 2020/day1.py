from typing import List
"""
--- Day 1: Report Repair ---
https://adventofcode.com/2020/day/1
"""

def sum_to_2020(expense_report: List[int]):

    for i in expense_report:
        for j in expense_report:
            for k in expense_report:
                if i != j and i != k and j != k and i > j >k :
                    if i + j + k == 2020:
                        return i * j * k

if __name__ in '__main__':

    expense_report = [
            1721,
            979,
            366,
            299,
            675,
            1456,
    ]

    with open('input.txt', 'r') as f:
        lines = [int(l.rstrip()) for l in f.readlines()]
        
        print(lines)
        print(sum_to_2020(lines))
