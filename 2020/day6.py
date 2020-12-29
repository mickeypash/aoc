
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
    lst = [x.replace('\n', ' ').split() for x in lst]

    groups = []
    for group in lst:
        answers = set()
        for a in group:
            if len(a) > 0:
                for i in a:
                    answers.add(i)
            else:
                answers.add(a)

        groups.append(answers)

    print(sum([len(g) for g in groups]))
