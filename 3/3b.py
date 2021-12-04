bit_length = 0
length = 0

diagnostic = []

def get_bit(value, bit_index):
    # bit_index is 0 indexed from the left ex:
    # for 0b00010, the `1` is located at bit_index 3
    return (value // (2 ** (bit_length - 1 - bit_index))) % 2

with open("input.txt") as fp: 
    while True: 
        line = fp.readline().strip()
        if not line: 
            break
        
        length += 1

        diagnostic.append(int(line, 2))

        if not bit_length:
            bit_length = len(line)


oxygen_generator = diagnostic.copy()
co2_scrubber = diagnostic.copy()

for bit_index in range(bit_length):
    if len(oxygen_generator) > 1:
        oxygen_generator_total = [0] * bit_length
        for oxygen_generator_value in oxygen_generator:
            for index in range(bit_length):
                oxygen_generator_total[index] += get_bit(oxygen_generator_value, index)

        criteria_gamma = 0
        for value in oxygen_generator_total:
            if value >= len(oxygen_generator) / 2:
                criteria_gamma += 1
            
            criteria_gamma <<= 1
        criteria_gamma >>= 1

        oxygen_generator = list(filter(lambda x: get_bit(x, bit_index) == get_bit(criteria_gamma, bit_index), oxygen_generator))


    if len(co2_scrubber) > 1:
        co2_scrubber_total = [0] * bit_length
        for co2_scrubber_value in co2_scrubber:
            for index in range(bit_length):
                co2_scrubber_total[index] += get_bit(co2_scrubber_value, index)

        print(co2_scrubber_total)

        criteria_epsilon = 0
        for value in co2_scrubber_total:
            if value < len(co2_scrubber) / 2:
                criteria_epsilon += 1
            
            criteria_epsilon <<= 1
        criteria_epsilon >>= 1

        co2_scrubber = list(filter(lambda x: get_bit(x, bit_index) == get_bit(criteria_epsilon, bit_index), co2_scrubber))


print(bin(oxygen_generator[0]))
print(bin(co2_scrubber[0]))
print(oxygen_generator[0] * co2_scrubber[0])

    