lst = open("input4.txt").read().splitlines()

test = [
    "2-4,6-8",
    "2-3,4-5",
    "5-7,7-9",
    "2-8,3-7",
    "6-6,4-6",
    "2-6,4-8",
]

def get_section(rng):
    start, stop = [int(i) for i in rng.split("-")]
    sections = [x for x in range(start, stop+1)]
    return set(sections)

part1 = 0
part2 = 0
for i in lst:
    elf1, elf2 = [get_section(x) for x in i.split(",")]

    if elf1.issubset(elf2) or elf2.issubset(elf1):
        part1 +=1

    if elf1.intersection(elf2):
        part2 +=1

print(part1)
print(part2)
