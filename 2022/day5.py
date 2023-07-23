EMPTY = ''


def load(lst):
    for line in lst:
        columns = line.split("    ")
        columns = [c.split(" ") for c in columns]

        clean_columns = []
        for c in columns:
            clean_columns += c

        yield (clean_columns)


def contents(crate):
    return crate.replace("[", "").replace("]", "")


def crate_mover_9000(stacks, instructions):
    # part 1 
    for line in instructions:
        num, _from, _to = int(line[1]), int(line[3]), int(line[5])
        for n in range(num):
            # print(stacks)
            stacks[_to-1].append(stacks[_from-1].pop())

    print("".join([s.pop() for s in stacks]))


def crate_mover_9001(stacks, instructions):
    # part 2
    for line in instructions:
        num, _from, _to = int(line[1]), int(line[3])-1, int(line[5])-1

        stacks[_to] += stacks[_from][-num:]
        stacks[_from] = stacks[_from][:-num]

        print(stacks)
    print("".join([s.pop() for s in stacks]))


if __name__ == "__main__":
    lst = open("input5.txt").read().splitlines()

    puzzle = list(load(lst))

    idx = puzzle.index([EMPTY])

    # -1 to remove the line numbering the stacks
    # +1 to remove the empty line
    dstacks, instructions = puzzle[:idx-1], puzzle[idx+1:]

    stacks = []
    for z in zip(*reversed(dstacks)):
        stacks.append([contents(c) for c in z if c is not EMPTY])

    crate_mover_9001(stacks, instructions)
