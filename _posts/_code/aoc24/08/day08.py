from typing import Tuple

# Set to False for part 1 and True for part 2
PART2 = False

def get_antinodes(loc1: Tuple[int, int], loc2: Tuple[int, int]):
    if PART2:
        register(loc1)
        register(loc2)

    dx = abs(loc1[0] - loc2[0])
    dy = abs(loc1[1] - loc2[1])

    # loc1 always has lower y, but we don't know about x
    if loc1[0] >= loc2[0]:
        cnt = 1
        while register((loc1[0] + dx * cnt, loc1[1] - dy * cnt)):
            if not PART2:
                break
            cnt += 1
        cnt = 1
        while register((loc2[0] - dx * cnt, loc2[1] + dy * cnt)):
            if not PART2:
                break
            cnt += 1
    else:
        cnt = 1
        while register((loc1[0] - dx * cnt, loc1[1] - dy * cnt)):
            if not PART2:
                break
            cnt += 1
        cnt = 1
        while register((loc2[0] + dx * cnt, loc2[1] + dy * cnt)):
            if not PART2:
                break
            cnt += 1

def register(node: Tuple[int, int]) -> None:
    global resonance
    y = len(resonance)
    x = len(resonance[0])
    # verify if node location is on grid
    if node[0] < 0 or node[1] < 0 or node[0] >= x or node[1] >= y:
        return False
    resonance[node[1]][node[0]] = 1
    return True

with open("./input.txt", "r") as f:
    lines = [l.strip() for l in f.readlines()]

ants = {}
for y, line in enumerate(lines):
    for x, val in enumerate(line):
        if val == ".":
            continue
        if val not in ants:
            ants[val] = [(x, y)]
        else:
            ants[val].append((x, y))

resonance = [[0 for a in range(len(lines[0]))] for b in range(len(lines))]
for ant in ants:
    for i in range(len(ants[ant])):
        # compare every antennae location combination
        for k in range(i+1, len(ants[ant])):
            get_antinodes(ants[ant][i], ants[ant][k])

print(f"Solution: {sum([sum(row) for row in resonance])}")