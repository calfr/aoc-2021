# Sonar Sweep

def input_parser(input_content):
    return [int(x) for x in input_content.strip().split("\n")]

def part_a(data):
    # A nice little one liner.
    # Uses a List Comprehension to compare each in the range with it's previous, and include it only where there's a match,
    # then get the length of matches (the 0 index doesn't have anything to compare to)
    return len([data[i] for i in range(1,len(data)) if data[i] > data[i-1]])

def part_b(data):
    # Modified the Part A solution slightly, ignoring the first 2, and summing a range of 3 rather than just comparing single entires.
    return len([data[i] for i in range(3,len(data)) if sum(data[i-2:i+1]) > sum(data[i-3:i])])

if __name__ == "__main__":
    data = input_parser(open("input.txt","r").read())
    print(f"Day 1 Part A solution: {part_a(data)}")
    print(f"Day 1 Part B solution: {part_b(data)}")