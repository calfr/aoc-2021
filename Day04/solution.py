# Dive!

def input_parser(input_content):
    # We have a single initial line, and then a sequence of boards.
    order = [int(x) for x in [y.split(",") for y in input_content.strip().split("\n")][0]]
    boards = []
    for board_data in input_content.strip().split("\n\n")[1:]:
        rows = [[int(y[i:i+2]) for i in range(0,13,3)] for y in board_data.split("\n")]
        board = rows
        boards.append(board)
    return (order, boards)

def is_board_solved(board,called):
    for row in board:
        if len(get_uncalled_numbers_for_list(row,called)) == 0:
            return True, row
    # check columns
    for i in range(5):
        column = [row[i] for row in board]
        if len(get_uncalled_numbers_for_list(column,called)) == 0:
            return True, column
    return False

def get_uncalled_numbers_for_board(board,called):
    uncalled_numbers = []
    for row in board:
        uncalled_numbers += get_uncalled_numbers_for_list(row,called)
    return set(uncalled_numbers)

def get_uncalled_numbers_for_list(l,called):
    return [x for x in l if x not in called]

def part_a(order,boards):
    for i in range(len(order)):
        for b in boards:
            if is_board_solved(b,order[:i+1]):
                return order[i] * sum(get_uncalled_numbers_for_board(b,order[:i+1]))

def part_b(order,boards):
    i = -1
    while len(boards) > 1:
        losing_boards = []
        i+=1
        for b in boards:
            if not is_board_solved(b,order[:i+1]):
                losing_boards.append(b)
        boards = losing_boards
    target = boards[0]
    while not is_board_solved(target,order[:i+1]):
        i+=1
    return order[i] * sum(get_uncalled_numbers_for_board(target,order[:i+1]))

if __name__ == "__main__":
    data = input_parser(open("input.txt","r").read())
    print(f"Day 4 Part A solution: {part_a(*data)}")
    print(f"Day 4 Part B solution: {part_b(*data)}")