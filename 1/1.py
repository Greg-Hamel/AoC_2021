larger_than_previous = 0
previous_depth = None

with open("input.txt") as fp: 
    while True: 
        line = fp.readline() 
        if not line: 
            break
        
        current_depth = int(line)  
        larger_than_previous += 1 if previous_depth and previous_depth < current_depth else 0
        previous_depth = current_depth

print(larger_than_previous)