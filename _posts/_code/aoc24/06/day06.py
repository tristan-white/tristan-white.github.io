import copy

RIGHT = 1
DOWN = 2
LEFT = 4
UP = 8

with open("./input.txt", "r") as f:
    rows = [list(l.strip()) for l in f.readlines()]

def run(rows):
    xgrid = [[0 for i in range(len(rows[0]))] for j in range(len(rows))]
    headings = [[0 for i in range(len(rows[0]))] for j in range(len(rows))]

    for y,r in enumerate(rows):
        if "^" in r:
            x = r.index("^")
            break

    dir = "up"
    while True:
        xgrid[y][x] = 1
        new_x = x
        new_y = y
        if dir == "up":
            if y == 0:
                break
            new_y -= 1
        if dir == "down":
            if y >= len(rows) - 1:
                break
            new_y += 1
        if dir == "right":
            if x >= len(rows[0]) - 1:
                break
            new_x += 1
        if dir == "left":
            if x < 0:
                break
            new_x -= 1
        
        if rows[new_y][new_x] == "#":
            if dir == "up":
                if headings[y][x] & UP:
                    return 0
                else:
                    headings[y][x] |= UP
                dir = "right"
            elif dir == "right":
                if headings[y][x] & RIGHT:
                    return 0
                else:
                    headings[y][x] |= RIGHT
                dir = "down"
            elif dir == "down":
                if headings[y][x] & DOWN:
                    return 0
                else:
                    headings[y][x] |= DOWN
                dir = "left"
            elif dir == "left":
                if headings[y][x] & LEFT:
                    return 0
                else:
                    headings[y][x] |= LEFT
                dir = "up"
            continue

        x = new_x
        y = new_y

    return sum(sum(r) for r in xgrid)

part2 = 0
for i in range(len(rows)):
    for j in range(len(rows[0])):
        print(i,j)
        if rows[i][j] != "#" and rows[i][j] != "^":
            temp_grid = copy.deepcopy(rows)
            temp_grid[i][j] = "#"
            if run(temp_grid) == 0:
                part2 += 1

print(f"Part 1: {run(rows)}")
print(f"Part 1: {part2}")