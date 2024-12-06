# Pardon my ugly code
part1 = 0
part2 = 0
rules = {}
incorrect = []

def check(update):
    for i in range(len(update)):
        # is cur in set of any later nums?
        for j in range(i,len(update)):
            if update[j] in rules:
                if update[i] in rules[update[j]]:
                    return 0

        # any earlier nums in set of cur?
        if update[i] in rules:
            for j in range(0,i):
                if update[j] in rules[update[i]]:
                    return 0
    return update[(len(update) - 1) // 2]

with open("./input.txt", "r") as f:
    line = f.readline()
    while line != "\n":
        l,r = line.split("|")
        l = int(l)
        r = int(r)
        if l not in rules:
            rules[l] = set()
        rules[l].add(r)
        line = f.readline()
    
    updates = []
    for l in f.readlines():
        cur = l.strip().split(",")
        updates.append([int(n) for n in cur])
    
    for update in updates:
        ret = check(update)
        part1 += ret
        if ret == 0:
            incorrect.append(update)
    
for update in incorrect:
    pages = []
    ret = 0
    while update:
        cur = update.pop()
        for i in range(len(pages) + 1):
            new_list = pages.copy()
            new_list.insert(i, cur)
            ret = check(new_list)
            if ret:
                pages = new_list.copy()
                break
    part2 += ret

print(f"Part 1: {part1}")
print(f"Part 2: {part2}")