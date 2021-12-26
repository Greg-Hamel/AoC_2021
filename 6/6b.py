from pprint import pprint
total_end_fish = 0

memoization = {}

def fish(days_before_next, number_days_left):
    # print(f"New Fish: {number_days_left} days left {days_before_next} days before reproduction")
    # print('memoized:')
    # print(memoization)
    fish_title  = f"{number_days_left}-{days_before_next}"

    if memoization.get(fish_title):
        # print(f"memoized fish:{fish_title}")
        return memoization.get(fish_title)
    
    recurvise_total_fish = 1
    for day in range(number_days_left):
        # print("here", days_before_next, day)
        if (days_before_next - day <= 0) and ((day - days_before_next) % 7 == 0):
            if number_days_left - day > 0:
                recurvise_total_fish += fish(9, number_days_left - day)
    
    # print(days_before_next, number_days_left)
    memoization[fish_title] = recurvise_total_fish

    return recurvise_total_fish

fish_values = []
for i in range(6):
    if i == 0: fish_values.append(0)
    else:
        fish_values.append(fish(i, 256))

with open("input.txt") as fp: 
    line = fp.readline().strip().split(',')
    for item in line:
        total_end_fish += fish_values[int(item)]

print(fish_values)
print(total_end_fish)


    
