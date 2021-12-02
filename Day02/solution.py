# Dive!

def input_parser(input_content):
    return [(x.split(" ")[0],x.split(" ")[1]) for x in input_content.strip().split("\n")]

def part_a(data):
    x,y = 0,0
    for entry in data:
        if entry[0] == "forward":
            x += int(entry[1])
        elif entry[0] == "down":
            y += int(entry[1])
        elif entry[0] == "up":
            y -= int(entry[1])
    return x*y

def part_b(data):
    x,y,aim = 0,0,0
    for entry in data:
        if entry[0] == "forward":
            x += int(entry[1])
            y += int(entry[1])*aim
        elif entry[0] == "down":
            aim += int(entry[1])
        elif entry[0] == "up":
            aim -= int(entry[1])
    return x*y

if __name__ == "__main__":
    data = input_parser(open("input.txt","r").read())
    print(f"Day 2 Part A solution: {part_a(data)}")
    print(f"Day 2 Part B solution: {part_b(data)}")