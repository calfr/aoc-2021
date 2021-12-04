# Dive!

def input_parser(input_content):
    return [x for x in input_content.strip().split("\n")]

def get_most_common_bit_value(data,index):
    sample = [z[index] for z in data]
    # Bit of a hack in combination with the solution parts - if we return 1 by default, and go by not-equal in part B, it'll cover the requirement
    # for when a value's of equal presidence. 
    if sample.count('0') > sample.count('1'):
        return 0
    else:
        return 1

def part_a(data):
    gamma, epsilon = 0,0
    change = 2**(len(data[0])-1)
    for i in range(len(data[0])):
        gamma += 0 if get_most_common_bit_value(data,i) == 0 else change
        epsilon += 0 if get_most_common_bit_value(data,i) == 1 else change
    return (gamma*epsilon)
        

def part_b(data):
    oxygen_sample = co2_sample = data
    index = 0
    while len(oxygen_sample) > 1 or len(co2_sample) > 1:
        if len(oxygen_sample) > 1:
            oxygen_sample = [a for a in oxygen_sample if a[index] == str(get_most_common_bit_value(oxygen_sample,index))]
        if len(co2_sample) > 1:
            co2_sample = [a for a in co2_sample if a[index] != str(get_most_common_bit_value(co2_sample,index))]
        index += 1
        print(oxygen_sample,co2_sample)
    
    return(int(oxygen_sample[0],2)*int(co2_sample[0],2))

if __name__ == "__main__":
    data = input_parser(open("input.txt","r").read())
    print(f"Day 3 Part A solution: {part_a(data)}")
    print(f"Day 3 Part B solution: {part_b(data)}")