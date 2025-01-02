with open("./input.txt", "r") as f:
    nums = f.read()[:-1]

ret = 0

num_ids = len(nums) // 2

id_start = 0
id_end = num_ids

j = len(nums) - 1 if len(nums) % 2 else len(nums) - 2

l_exp_pos = 0
r_exp_pos = 0

fifo = []

for i in range(len(nums)):
    # get current num
    n = int(nums[i])

    if id_start >= id_end + 1:
        break
    if i % 2 == 0:
        print("even")
        for _ in range(n):
            ret += l_exp_pos * id_start
            print(l_exp_pos, id_start)
            l_exp_pos += 1
        id_start += 1
    else:
        print("odd")
        for _ in range(n):
            if not fifo:
                # get last id
                for x in range(int(nums[j])):
                    fifo.append(id_end)
                print(fifo)
                j -= 2
                id_end -= 1
            # multiply the id by the pos in expanded array
            popped = fifo.pop(0)
            print(l_exp_pos, popped)
            ret += popped * l_exp_pos
            l_exp_pos += 1

for n in fifo:
    ret += n * l_exp_pos
    l_exp_pos += 1

print(ret)