position = [0, 0] # horizontal position, depth 
aim = 0

directional_values = { 
  "down": 1,
  "up": -1,
}

with open("input.txt") as fp: 
    while True: 
        line = fp.readline() 
        if not line: 
            break
        
        direction, amount = line.split(' ')
        amount = int(amount)
        if direction == 'forward':
            position = [position[0] + amount, position[1] + aim * amount]
        else:
            aim += directional_values[direction] * amount

print(position[0] * position[1])