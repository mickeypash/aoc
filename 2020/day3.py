
HIT  = "X"
MISS = "O"

TREE = "#"
SNOW = "."

if __name__ == '__main__':

    f = open("input3.txt", "r")

    lines = f.read().splitlines()

    count_hits = 0
    count_misses = 0

    for i in range(0, len(lines)):
        idx = i*3 % len(lines[i]) 
        something = lines[i][idx]
        if something == TREE:
            print(something)
            count_hits += 1
        if something == SNOW:
            count_misses += 1

    print(count_hits)
    print(count_misses)

    f.close()
