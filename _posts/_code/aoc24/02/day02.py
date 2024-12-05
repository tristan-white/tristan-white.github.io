def is_safe_w_dampen(nums, i):
    copy1 = nums.copy()
    copy2 = nums.copy()
    copy3 = nums.copy()
    copy1.pop(i)
    copy2.pop(i+1)
    if i > 0:
        copy3.pop(i-1)
    one = is_safe(copy1, False)
    two = is_safe(copy2, False)
    three = is_safe(copy3, False)
    return one or two or three

def is_safe(nums, dampen: bool) -> bool: 
    increasing = True if nums[1] > nums[0] else False
    for i in range(len(nums) - 1):
        diff = nums[i+1] - nums[i]
        if (diff == 0 or diff > 3 or diff < -3) \
        or (diff > 0 and not increasing) \
        or (diff < 0 and increasing):
            if dampen:
                return is_safe_w_dampen(nums, i)
            return False
    return True

with open("input.txt", "r") as f:
    lines = f.readlines()

part1 = 0
part2 = 0
for line in lines:
    nums = [int(x) for x in line.split()]

    if is_safe(nums, False):
        part1 += 1
    if is_safe(nums, True):
        part2 += 1

print(f"Part 1 solution: {part1}") 
print(f"Part 2 solution: {part2}")