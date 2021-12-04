larger_than_previous = 0

def sum_of_three(array):
    return array[0] + array[1] + array[2]

with open("input.txt") as fp: 
    rolling_buffer = [] # Buffer of 4 elements

    while True: 
        line = fp.readline() 
        if not line: 
            break
        
        rolling_buffer.append(int(line))
        if len(rolling_buffer) == 4:
            previous_value = sum_of_three(rolling_buffer)
            rolling_buffer.pop(0)
            current_value = sum_of_three(rolling_buffer)
            larger_than_previous += 1 if previous_value and previous_value < current_value else 0


print(larger_than_previous)