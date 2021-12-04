position = [0, 0] # horizontal position, depth 

directional_values = { 
  "forward": [0, 1], # index of application, positivity
  "down": [1, 1],
  "up": [1, -1],
}

with open("input.txt") as fp: 
    while True: 
        line = fp.readline() 
        if not line: 
            break
        
        direction, amount = line.split(' ')
        position[directional_values[direction][0]] += directional_values[direction][1] * int(amount)

print(position[0] * position[1])