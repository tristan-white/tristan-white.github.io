import re

with open("./input.txt", "r") as f:
    data = f.read()

enabled = True
pattern = r'mul\((\d{1,3}),(\d{1,3})\)|(do\(\))|(don\'t\(\))'
matches = re.findall(pattern, data)
part1 = 0
part2 = 0
for m in matches:
    if m[2]:
        enabled = True
    elif m[3]:
        enabled = False
    else:
        cur = int(m[0]) * int(m[1])
        part1 += cur
        if enabled:
            part2 += cur

print(f"Part 1: {part1}")
print(f"Part 2: {part2}")