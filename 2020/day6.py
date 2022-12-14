
lines = """
abc

a
b
c

ab
ac

a
a
a
a

b
"""

with open('input6.txt', 'r') as file:
    lst = file.read().split('\n\n')
    lst = lines.split('\n\n')

    lst = [x.replace('\n', ' ').split() for x in lst]

    groups = []
    for group in lst:
        answers = []
        for answer in group:
            answers.append(set(answer))
        groups.append(answers)

    # print(sum([len(g) for g in groups]))
