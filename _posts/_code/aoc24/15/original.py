from dataclasses import dataclass
SPACE = 0
WALL = 1
BOX = 2
BOT = 3

class Box2():
    xL: int
    xR: int
    y: int

    def move(self, ):

@dataclass
class Pos():
    x: int
    y: int

    def add(self, p: 'Pos'):
        return Pos(self.x + p.x, self.y + p.y)

with open("input.txt", "r") as f:
    line = f.readline()
    grid = []
    while line != "\n":
        grid.append([letter for letter in line.strip()])
        line = f.readline()
    movements = f.read().replace('\n', '')

def print_grid():
    for row in grid:
        print(row)

print_grid()

def update(cur: Pos, dir: Pos):
    # global grid
    next_pos = cur.add(dir)
    next_obj = grid[next_pos.y][next_pos.x]
    move = False
    # print(cur, dir)

    if next_obj == ".":
        move = True

    elif next_obj == "O":
        move = update(next_pos, dir)

    elif next_obj == "#":
        return False
    
    if move:
        grid[next_pos.y][next_pos.x] = grid[cur.y][cur.x]
        grid[cur.y][cur.x] = '.'
    return move

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
    if update(bot, dir):
        bot = bot.add(dir)

def calc_gps():
    # global grid
    ret = 0
    for row in range(len(grid)):
        for col in range(len(grid[0])):
            if grid[row][col] == "O":
                ret += 100 * row + col
    return ret

print()
print_grid()

ret = calc_gps()
print(f"{ret}")