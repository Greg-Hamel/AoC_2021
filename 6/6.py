fish_1 = [1]
fish_1_day_count = []
total_end_fish = 0

## calculate function values for a "1" fish
for day in range(80):
    new_fish = []
    number_to_add = 0

    for fish in fish_1:
        if fish == 0:
            new_fish.append(6)
            number_to_add += 1
        else: 
            new_fish.append(fish - 1)
    
    new_fish += [8] * number_to_add
    fish_1_day_count.append(len(new_fish))
    fish_1 = new_fish

# Using the "1" fish calculation,
# evaluate every other fish end values

print(fish_1_day_count)

fish_values = [0] * 6
for i in range(6):
    if i == 0:
        continue
    fish_values[i] = fish_1_day_count[-1 * i]

print(fish_values)

with open("input.txt") as fp: 
    line = fp.readline().strip().split(',')
    for item in line:
        total_end_fish += fish_values[int(item)]

print(total_end_fish)


    
