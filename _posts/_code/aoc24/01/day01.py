left = []
right = []

# https://adventofcode.com/2024/day/1/input
with open("input.txt", "r") as f:
    lines = f.readlines()

for line in lines:
    l,r = line.split()
    left.append(int(l))
    right.append(int(r))

left.sort()
right.sort()

part1 = 0
part2 = 0
for i,l in enumerate(left):
    diff = left[i] - right[i]
    if diff < 0:
        diff *= -1
    part1 += diff

    matches = 0
    for r in right:
        if l == r:
            matches += 1
    part2 += l * matches

print(f"Part 1 solution: {part1}") 
print(f"Part 2 solution: {part2}") 