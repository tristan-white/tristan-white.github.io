with open("./input.txt", "r") as f:
    nums = [int(n) for n in f.read()[:-1]]

ret = 0
stack = []
disk_pos = 0
last_file_index = len(nums) - 1 if len(nums) % 2 else len(nums) - 2
id_r = nums[last_file_index // 2]
id_l = 0

for i in range(len(nums)):
    if id_l >= id_r + 1:
        break

    size = nums[i]

    if i % 2 == 0:
        for _ in size:
            ret += id_l * disk_pos
            disk_pos += 1
        id_l += 1

    else:
        # get size of last file
        last_file_size = last_file_index
        cur_gap_size = size
        j = i
        moved = True
        
        while cur_gap_size < last_file_size:
            j += 2
            if j > len(nums - 1):
                moved = False
                break
            cur_gap_size = nums[j]
        if moved:
            stack.append((last_file_size, id_r))
            

        

print(ret)