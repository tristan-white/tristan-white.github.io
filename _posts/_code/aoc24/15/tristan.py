from typing import Tuple, Optional
from dataclasses import dataclass, field

RED = "\033[31m"
RESET = "\033[0m"

@dataclass
class Pos():
    x: int
    y: int

    # Return True if move happend
    def move_dir(self, dir: 'Pos'):
        p = self + dir
        c = grid[p.y][p.x] 
        if c == "#":
            return False
        elif c == "O":
            if not p.move_dir(dir):
                return False
        elif c == "[":
            b = Box(p, Pos(p.x + 1, p.y))
            if not b.move_dir(dir):
                return False
        elif c == "]":
            b = Box(Pos(p.x - 1, p.y), p)
            if not b.move_dir(dir):
                return False
        # print(self, p, dir)
        if not grid[p.y][p.x] == '.':
            print_grid(grid, p)
            exit()
        grid[p.y][p.x] = grid[self.y][self.x]
        grid[self.y][self.x] = "."
        return True

    def __add__(self, other: 'Pos'):
        return Pos(self.x + other.x, self.y + other.y)
    
    def __eq__(self, other: 'Pos'):
        return self.x == other.x and self.y == other.y
    

@dataclass
class Box():
    l: Pos
    r: Pos

    def move_dir(self, dir: Pos):
        # create box in the new position
        b = Box(self.l + dir, self.r + dir)
        cl = grid[b.l.y][b.l.x]
        cr = grid[b.r.y][b.r.x]
        if cl == "#" or cr == "#":
            return False
        elif cl == "[" and cr == "]":
            # movement is vertical
            if not b.move_dir(dir):
                return False
        elif cl == "]" and cr == "[":
            # movement is horizontal
            if not b.move_dir(dir):
                return False
        # TODO: count for case where cl = ] and cr == [ but movement is vertical
        elif cl == "]":
            # create box to left of b. doesn't matter if box is up or down
            left_box = Box(Pos(b.l.x - 1, b.l.y), b.l)
            print(self, dir)
            if not left_box.move_dir(dir):
                return False
        elif cr == "[":
            # create box to right of b. doesn't matter if box is up or down
            right_box = Box(b.r, Pos(b.r.x + 1, b.r.y))
            if not right_box.move_dir(dir):
                return False
        assert cl == "." and cr == "."
        # set next spot to cur and cur to "."
        grid[b.l.y][b.l.x] = grid[self.l.y][self.l.x]
        grid[b.r.y][b.r.x] = grid[self.r.y][self.r.x]
        grid[self.l.y][self.l.x] = "."
        grid[self.r.y][self.r.x] = "."
        return True


with open("input.txt", "r") as f:
    line = f.readline()
    temp = []
    while line != "\n":
        temp.append([letter for letter in line.strip()])
        line = f.readline()
    movements = f.read().replace('\n', '')

# transform grid for part 2
grid = []
for r in range(len(temp)):
    grid.append([])
    for c in range(len(temp[0])):
        if temp[r][c] == "#":
            grid[r].append("#")
            grid[r].append("#")
        elif temp[r][c] == ".":
            grid[r].append(".")
            grid[r].append(".")
        elif temp[r][c] == "O":
            grid[r].append("[")
            grid[r].append("]")
        elif temp[r][c] == "@":
            grid[r].append("@")
            grid[r].append(".")

def print_grid(grid, debug_spot: Pos):
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            if grid[i][j] == "@":
                print(RED + '@' + RESET, end="")
            elif debug_spot.y == i and debug_spot.x == j:
                print(RED + grid[i][j] + RESET, end="")
            else:
                print(grid[i][j], end="")
        print()
            

# find robot
def find_bot():
    for row in range(len(grid)):
        for col in range(len(grid[0])):
            if grid[row][col] == "@":
                return Pos(x=col, y=row)

bot = find_bot()

for mov in movements:
    if mov == "<":
        dir = Pos(-1, 0)
    elif mov == "v":
        dir = Pos(0, +1)
    elif mov == ">":
        dir = Pos(1, 0)
    elif mov == "^":
        dir = Pos(0, -1)
    if bot.move_dir(dir):
        bot = bot + dir

def calc_gps(box_char: str):
    # global grid
    ret = 0
    for row in range(len(grid)):
        for col in range(len(grid[0])):
            if grid[row][col] == box_char:
                ret += 100 * row + col
    return ret

print()
print_grid(grid)

ret = calc_gps("[")
print(f"{ret}")

# 1531312 > ? < 1541368