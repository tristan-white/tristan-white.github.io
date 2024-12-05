with open("input.txt", "r") as f:
    lines = [l[:-1] for l in f.readlines()]

part1 = 0
part2 = 0
rows = len(lines)
cols = len(lines[0])

for i in range(rows):
    for j in range(cols):
        # part 1
        words = []
        if j <= cols - 4:
            words.append(lines[i][j] + lines[i][j+1] + lines[i][j+2] + lines[i][j+3])
        if i <= rows - 4 and j <= cols - 4:
            words.append(lines[i][j] + lines[i+1][j+1] + lines[i+2][j+2] + lines[i+3][j+3])
        if i <= rows - 4:
            words.append(lines[i][j] + lines[i+1][j] + lines[i+2][j] + lines[i+3][j])
        if i <= rows - 4 and j > 2:
            words.append(lines[i][j] + lines[i+1][j-1] + lines[i+2][j-2] + lines[i+3][j-3])
        if j > 2:
            words.append(lines[i][j] + lines[i][j-1] + lines[i][j-2] + lines[i][j-3])
        if j > 2 and i > 2:
            words.append(lines[i][j] + lines[i-1][j-1] + lines[i-2][j-2] + lines[i-3][j-3])
        if i > 2:
            words.append(lines[i][j] + lines[i-1][j] + lines[i-2][j] + lines[i-3][j])
        if i > 2 and j <= cols - 4:
            words.append(lines[i][j] + lines[i-1][j+1] + lines[i-2][j+2] + lines[i-3][j+3])
        part1 += sum(1 for w in words if w == "XMAS")

        # part 2
        if j > 1 and i > 1:
            up_left = lines[i][j] + lines[i-1][j-1] + lines[i-2][j-2]
            up_right = lines[i][j-2] + lines[i-1][j-1] + lines[i-2][j]
            if i == 2 and j == 3:
                print(up_left, up_right)
            if (up_left == "MAS" or up_left == "SAM") and (up_right == "MAS" or up_right == "SAM"):
                part2 += 1

print(f"Part1: {part1}")
print(f"Part2: {part2}")