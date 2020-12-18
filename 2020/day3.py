
TREE = "#"
SNOW = "."

def part2(lines, right, down):

    count_hits = 0
    count_misses = 0
    count = 0

    for row in range(0, len(lines), down):
        
        col = count * right % len(lines[row])
        something = lines[row][col]
        #print(lines[row])
        if something == TREE:
            count_hits += 1
        if something == SNOW:
            count_misses += 1

        count +=1

    return count_hits

def test_slopes(slopes):
    multiplicative_hits = 1

    for slope in slopes:
        multiplicative_hits *= (part2(lines, *slope))

    return multiplicative_hits


if __name__ == '__main__':

    f = open("input3.txt", "r")

    lines = f.read().splitlines()

    slopes = [
            (1, 1),
            (3, 1),
            (5, 1),
            (7, 1),
            (1, 2)
    ]

    print(test_slopes(slopes))

    f.close()

"""
.##......#.##..#..#..##....#...
#....##....#.....#.....#..##.##
##..........#....#.#...#.......
.#.##........#..............#..
"""
