diagnostic_total = [0] * 12
length=0
gamma = 0

with open("input.txt") as fp: 
    while True: 
        line = fp.readline().strip()
        if not line: 
            break
        
        length += 1
        for index, value in enumerate(line):
            diagnostic_total[index] += int(value)
        
for value in diagnostic_total:
    if value > length / 2:
        gamma += 1
    gamma <<= 1
gamma >>= 1

epsilon = gamma ^ 0b111111111111

print(gamma * epsilon)

