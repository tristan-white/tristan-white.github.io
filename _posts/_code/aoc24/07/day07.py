MUL = 0
ADD = 1
CAT = 2

# set to 1 or 2 to get answer for part 1 or 2
PART = 2

def get_ins(n):
    instructions = []
    while n >= 0:
        instructions.append(n % (PART + 1))
        n //= (PART + 1)
        if n == 0:
            break
    return instructions

if __name__ == "__main__":
    with open("./input.txt", "r") as f:
        lines = [l[:-1] for l in f.readlines()]
    
    ans = 0
    for line in lines:
        parts = line.split(":")
        target = int(parts[0])
        operands = parts[1].strip().split(" ")

        # total possible permutations of equations
        total = (PART + 1) ** (len(operands) - 1)
        for n in range(total):
            ins = get_ins(n)
            cur = 0
            while len(ins) < len(operands) - 1:
                ins.append(0)
            res = int(operands[0])
            for o in operands[1:]:
                i = ins[cur]
                if i == MUL:
                    res *= int(o)
                elif i == ADD:
                    res += int(o)
                elif i == CAT:
                    res = int(str(res) + o)
                cur += 1
            if target == res:
                ans += target
                break

    print(ans)