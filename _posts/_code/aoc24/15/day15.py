from typing import Tuple, Optional
from dataclasses import dataclass, field
SPACE = 0
WALL = 1
BOX = 2
BOT = 3

RED = "\033[31m"
RESET = "\033[0m"

@dataclass
class Pos():
    x: int
    y: int

    def add(self, p: 'Pos'):
        return Pos(self.x + p.x, self.y + p.y)
    
    def __eq__(self, other: 'Pos'):
        return self.x == other.x and self.y == other.y
    
def get_spot_avail(next_pos: Pos, dir: Pos) -> Tuple[bool, Optional['Box']]:
    next_obj = grid[next_pos.y][next_pos.x]
    if next_obj == ".":
        return True, None
    elif next_obj == "[":
        box = Box(next_pos, Pos(next_pos.x + 1, next_pos.y))
        return box.can_move(dir), box
    elif next_obj == "]":
        box = Box(Pos(next_pos.x - 1, next_pos.y), next_pos)
        return box.can_move(dir), box
    elif next_obj == "#":
        return False, None

@dataclass
class Box():
    l: Pos
    r: Pos
    child_l: Optional['Box'] = field(default=None)
    child_r: Optional['Box'] = field(default=None)

    def overlaps(self, pos: Pos) -> bool:
        return pos == self.l or pos == self.r

    def move(self, dir: Pos):
        next_box_spot = Box(self.l.add(dir), self.r.add(dir))
        if self.child_l:
            self.child_l.move(dir)
        if self.child_r:
            self.child_r.move(dir)
        if self.can_move(dir):
            grid[self.l.y][self.l.x] = "."
            grid[self.r.y][self.r.x] = "."
            grid[next_box_spot.l.y][next_box_spot.l.x] = "["
            grid[next_box_spot.r.y][next_box_spot.r.x] = "]"

    def can_move(self, dir: Pos) -> bool:
        next_box_spot = Box(self.l.add(dir), self.r.add(dir))
        move_l = False
        move_r = False

        if not self.overlaps(next_box_spot.l):
            move_l, self.child_l = get_spot_avail(next_box_spot.l, dir)
        else:
            move_l = True

        if not self.overlaps(next_box_spot.r):
            move_r, self.child_r = get_spot_avail(next_box_spot.r, dir)
        else:
            move_r = True

        if move_l and move_r:
            return True
        return False


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

def print_grid():
    for row in grid:
        if "@" in row:
            print(RED + "".join(row) + RESET)
        else:
            print("".join(row))


print_grid()

def move_robot(cur: Pos, dir: Pos):
    next_pos = cur.add(dir)

    can_move, child_box = get_spot_avail(next_pos, dir)
    if can_move:
        if child_box:
            child_box.move(dir)
        grid[next_pos.y][next_pos.x] = '@'
        grid[cur.y][cur.x] = '.'
        return True
    return False

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
    if move_robot(bot, dir):
        bot = bot.add(dir)

def calc_gps(box_char: str):
    # global grid
    ret = 0
    for row in range(len(grid)):
        for col in range(len(grid[0])):
            if grid[row][col] == box_char:
                ret += 100 * row + col
    return ret

print()
print_grid()

ret = calc_gps("[")
print(f"{ret}")

# 1531312 > ? < 1541368