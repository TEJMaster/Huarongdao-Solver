import sys
from queue import PriorityQueue
initial_state = [[0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0]]


class State:

    def __init__(self, parent=None):
        self.total_cost = 0
        if parent is None:
            self.board = initial_state
            self.cost = 0
            self.parent = None
            self.update_total_cost()
        else:
            self.board = []
            for i in range(5):
                self.board.append(parent.board[i].copy())
            self.cost = parent.cost + 1
            self.parent = parent

    def __gt__(self, other):
        return self.total_cost > other.total_cost

    def __lt__(self, other):
        return self.total_cost < other.total_cost

    def update_total_cost(self):
        self.total_cost = self.cost + get_heuristic(self)


def get_cao_location(state):
    for row in range(5):
        for column in range(4):
            if state.board[row][column] == 1:
                return row, column


def get_heuristic(state):
    cao_location = get_cao_location(state)
    return abs(cao_location[0] - 3) + abs(cao_location[1] - 1)
    # return abs(cao_location[0] - 3)*2 + abs(cao_location[1] - 1)       #79097
    # return abs(cao_location[0] - 3)                                    #94503
    # return pow(abs(cao_location[0] - 3),2) + abs(cao_location[1] - 1)   #59180
    # return pow(abs(cao_location[0] - 3), 3) + abs(cao_location[1] - 1)  # 18713 best ***
    # return pow(abs(cao_location[0] - 3),4) + abs(cao_location[1] - 1)  #20223


def read_file(file_name):
    with open(file_name) as file:
        lines = file.readlines()
        lines = [line.rstrip() for line in lines]
    for i in range(len(lines)):
        line = lines[i]
        for j in range(len(line)):
            initial_state[i][j] = int(line[j])


def get_empty(state):
    empty = []
    for row in range(5):
        for column in range(4):
            if state.board[row][column] == 0:
                empty.append((row, column))
    return empty


def move_single_piece(state, row, column):
    next_states = []
    # move up
    if row < 4 and state.board[row + 1][column] == 7:
        next_state = State(state)
        next_state.board[row][column] = 7
        next_state.board[row + 1][column] = 0
        next_state.update_total_cost()
        next_states.append(next_state)
    # move down
    if row > 0 and state.board[row - 1][column] == 7:
        next_state = State(state)
        next_state.board[row][column] = 7
        next_state.board[row - 1][column] = 0
        next_state.update_total_cost()
        next_states.append(next_state)
    # move left
    if column < 3 and state.board[row][column + 1] == 7:
        next_state = State(state)
        next_state.board[row][column] = 7
        next_state.board[row][column + 1] = 0
        next_state.update_total_cost()
        next_states.append(next_state)
    # move right
    if column > 0 and state.board[row][column - 1] == 7:
        next_state = State(state)
        next_state.board[row][column] = 7
        next_state.board[row][column - 1] = 0
        next_state.update_total_cost()
        next_states.append(next_state)
    return next_states


def move_double_piece(state, row1, column1, row2, column2):
    next_states = []
    # move 1x2 up
    if row1 == row2 < 4 and abs(column1 - column2) == 1 and \
            1 < state.board[row1 + 1][column1] == state.board[row2 + 1][column2] < 7:
        num = state.board[row1 + 1][column1]
        next_state = State(state)
        next_state.board[row1][column1], next_state.board[row2][column2] = num, num
        next_state.board[row1 + 1][column1], next_state.board[row2 + 1][column2] = 0, 0
        next_state.update_total_cost()
        next_states.append(next_state)
    # move 1x2 down
    if row1 == row2 > 0 and abs(column1 - column2) == 1 and \
            1 < state.board[row1 - 1][column1] == state.board[row2 - 1][column2] < 7:
        num = state.board[row1 - 1][column1]
        next_state = State(state)
        next_state.board[row1][column1], next_state.board[row2][column2] = num, num
        next_state.board[row1 - 1][column1], next_state.board[row2 - 1][column2] = 0, 0
        next_state.update_total_cost()
        next_states.append(next_state)
    # move 1x2 left
    if column1 < 2 and 1 < state.board[row1][column1 + 1] == state.board[row1][column1 + 2] < 7:
        num = state.board[row1][column1 + 1]
        next_state = State(state)
        next_state.board[row1][column1], next_state.board[row1][column1 + 1] = num, num
        next_state.board[row1][column1 + 2] = 0
        next_state.update_total_cost()
        next_states.append(next_state)
    if column2 < 2 and 1 < state.board[row2][column2 + 1] == state.board[row2][column2 + 2] < 7:
        num = state.board[row2][column2 + 1]
        next_state = State(state)
        next_state.board[row2][column2], next_state.board[row2][column2 + 1] = num, num
        next_state.board[row2][column2 + 2] = 0
        next_state.update_total_cost()
        next_states.append(next_state)
    # move 1x2 right
    if column1 > 1 and 1 < state.board[row1][column1 - 1] == state.board[row1][column1 - 2] < 7:
        num = state.board[row1][column1 - 1]
        next_state = State(state)
        next_state.board[row1][column1], next_state.board[row1][column1 - 1] = num, num
        next_state.board[row1][column1 - 2] = 0
        next_state.update_total_cost()
        next_states.append(next_state)
    if column2 > 1 and 1 < state.board[row2][column2 - 1] == state.board[row2][column2 - 2] < 7:
        num = state.board[row2][column2 - 1]
        next_state = State(state)
        next_state.board[row2][column2], next_state.board[row2][column2 - 1] = num, num
        next_state.board[row2][column2 - 2] = 0
        next_state.update_total_cost()
        next_states.append(next_state)

    # move 2x1 up
    if row1 < 3 and 1 < state.board[row1 + 1][column1] == state.board[row1 + 2][column1] < 7:
        num = state.board[row1 + 1][column1]
        next_state = State(state)
        next_state.board[row1][column1], next_state.board[row1 + 1][column1] = num, num
        next_state.board[row1 + 2][column1] = 0
        next_state.update_total_cost()
        next_states.append(next_state)
    if row2 < 3 and 1 < state.board[row2 + 1][column2] == state.board[row2 + 2][column2] < 7:
        num = state.board[row2 + 1][column2]
        next_state = State(state)
        next_state.board[row2][column2], next_state.board[row2 + 1][column2] = num, num
        next_state.board[row2 + 2][column2] = 0
        next_state.update_total_cost()
        next_states.append(next_state)
    # move 2x1 down
    if row1 > 1 and 1 < state.board[row1 - 1][column1] == state.board[row1 - 2][column1] < 7:
        num = state.board[row1 - 1][column1]
        next_state = State(state)
        next_state.board[row1][column1], next_state.board[row1 - 1][column1] = num, num
        next_state.board[row1 - 2][column1] = 0
        next_state.update_total_cost()
        next_states.append(next_state)
    if row2 > 1 and 1 < state.board[row2 - 1][column2] == state.board[row2 - 2][column2] < 7:
        num = state.board[row2 - 1][column2]
        next_state = State(state)
        next_state.board[row2][column2], next_state.board[row2 - 1][column2] = num, num
        next_state.board[row2 - 2][column2] = 0
        next_state.update_total_cost()
        next_states.append(next_state)
    # move 2x1 left
    if column1 == column2 < 3 and abs(row1 - row2) == 1 and \
            1 < state.board[row1][column1 + 1] == state.board[row2][column2 + 1] < 7:
        num = state.board[row1][column1 + 1]
        next_state = State(state)
        next_state.board[row1][column1], next_state.board[row2][column2] = num, num
        next_state.board[row1][column1+1], next_state.board[row2][column2+1] = 0, 0
        next_state.update_total_cost()
        next_states.append(next_state)
    # move 2x1 right
    if column1 == column2 > 0 and abs(row1 - row2) == 1 and \
            1 < state.board[row1][column1 - 1] == state.board[row2][column2 - 1] < 7:
        num = state.board[row1][column1 - 1]
        next_state = State(state)
        next_state.board[row1][column1], next_state.board[row2][column2] = num, num
        next_state.board[row1][column1-1], next_state.board[row2][column2-1] = 0, 0
        next_state.update_total_cost()
        next_states.append(next_state)
    return next_states


def move_cao(state, row1, column1, row2, column2):
    next_states = []
    # move Cao Cao up
    if row1 == row2 < 3 and abs(column1 - column2) == 1 and \
            state.board[row1 + 1][column1] == state.board[row2 + 1][column2] == 1:
        next_state = State(state)
        next_state.board[row1][column1], next_state.board[row2][column2] = 1, 1
        next_state.board[row1 + 1][column1], next_state.board[row2 + 1][column2] = 1, 1
        next_state.board[row1 + 2][column1], next_state.board[row2 + 2][column2] = 0, 0
        next_state.update_total_cost()
        next_states.append(next_state)
    # move Cao Cao down
    if row1 == row2 > 1 and abs(column1 - column2) == 1 and \
            state.board[row1 - 1][column1] == state.board[row2 - 1][column2] == 1:
        next_state = State(state)
        next_state.board[row1][column1], next_state.board[row2][column2] = 1, 1
        next_state.board[row1 - 1][column1], next_state.board[row2 - 1][column2] = 1, 1
        next_state.board[row1 - 2][column1], next_state.board[row2 - 2][column2] = 0, 0
        next_state.update_total_cost()
        next_states.append(next_state)
    # move Cao Cao left
    if column1 == column2 < 2 and abs(row1 - row2) == 1 and \
            state.board[row1][column1 + 1] == state.board[row2][column2 + 1] == 1:
        next_state = State(state)
        next_state.board[row1][column1], next_state.board[row2][column2] = 1, 1
        next_state.board[row1][column1+1], next_state.board[row2][column2+1] = 1, 1
        next_state.board[row1][column1 + 2], next_state.board[row2][column2 + 2] = 0, 0
        next_state.update_total_cost()
        next_states.append(next_state)
    # move Cao Cao right
    if column1 == column2 > 1 and abs(row1 - row2) == 1 and \
            state.board[row1][column1 - 1] == state.board[row2][column2 - 1] == 1:
        next_state = State(state)
        next_state.board[row1][column1], next_state.board[row2][column2] = 1, 1
        next_state.board[row1][column1-1], next_state.board[row2][column2-1] = 1, 1
        next_state.board[row1][column1 - 2], next_state.board[row2][column2 - 2] = 0, 0
        next_state.update_total_cost()
        next_states.append(next_state)
    return next_states


def run_move(state):
    white_space = get_empty(state)
    next_states = []
    row1, column1 = white_space[0][0], white_space[0][1]
    row2, column2 = white_space[1][0], white_space[1][1]
    next_states.extend(move_cao(state, row1, column1, row2, column2))
    next_states.extend(move_double_piece(state, row1, column1, row2, column2))

    next_states.extend(move_single_piece(state, row1, column1))
    next_states.extend(move_single_piece(state, row2, column2))
    return next_states


def check_goal(state):
    if state.board[3][1] == state.board[3][2] == state.board[4][1] == state.board[3][2] == 1:
        return True
    else:
        return False


def print_state(state):
    string = ''
    for row in range(5):
        for column in range(4):
            if state.board[row][column] == 0:
                string += '0'
            elif state.board[row][column] == 7:
                string += '4'
            elif state.board[row][column] == 1:
                string += '1'
            elif 1 < state.board[row][column] < 7 and column < 3 \
                    and state.board[row][column] == state.board[row][column+1]:
                string += '2'
            elif 1 < state.board[row][column] < 7 and column > 0 \
                    and state.board[row][column] == state.board[row][column-1]:
                string += '2'
            elif 1 < state.board[row][column] < 7 and row < 4 \
                    and state.board[row][column] == state.board[row+1][column]:
                string += '3'
            elif 1 < state.board[row][column] < 7 and row > 0 \
                    and state.board[row][column] == state.board[row-1][column]:
                string += '3'

            # string += str(state.board[row][column])
        string += '\n'
    string += '\n'
    return string


def print_string(state):
    string = ''
    for row in range(5):
        for column in range(4):
            if state.board[row][column] in range(2, 7):  # replace rectangle to r
                if 1 < state.board[row][column] < 7 and row < 4 \
                     and state.board[row][column] == state.board[row + 1][column]:
                    string += 'r'
                elif 1 < state.board[row][column] < 7 and row > 0 \
                    and state.board[row][column] == state.board[row - 1][column]:
                    string += 'r'
                else:
                    string += str(state.board[row][column])
            else:
                string += str(state.board[row][column])
    return string


def print_path(state, array):
    while state.parent is not None:
        array.append(print_state(state))
        state = state.parent
    else:
        array.append(print_state(state))


def a_star_search(location):
    frontier_queue = PriorityQueue()
    c1 = State()
    frontier_queue.put((c1.total_cost, c1))
    explored_set = set()
    while frontier_queue.empty() is False:
        min_state = frontier_queue.get()[1]

        # print(get_heuristic(min_state), min_state.board, min_state.cost, min_state.total_cost)
        if check_goal(min_state):
            f = open(location, 'a')
            f.write("Cost of the solution: " + str(min_state.cost) + '\n')
            array = []
            print_path(min_state, array)
            for i in range(len(array) - 1, -1, -1):
                f.write(array[i])
            return True
        if print_string(min_state) in explored_set:
            continue
        explored_set.add(print_string(min_state))
        moves = run_move(min_state)

        for item in moves:
            frontier_queue.put((item.total_cost, item))
    return False


def dfs_search(location):
    frontier_stack = []
    c2 = State()
    frontier_stack.append(c2)
    explored_set = set()
    explored_set.add(c2)
    while len(frontier_stack) != 0:
        last_state = frontier_stack.pop(-1)
        moves = run_move(last_state)
        for move in moves:
            if check_goal(move):
                f = open(location, 'a')
                f.write("Cost of the solution: " + str(move.cost) + '\n')
                array = []
                print_path(move, array)
                for i in range(len(array) - 1, -1, -1):
                    f.write(array[i])
                return True
            if print_string(move) not in explored_set:
                explored_set.add(print_string(move))
                frontier_stack.append(move)
    return False


def main(args):
    read_file(args[1])
    dfs_search(args[2])
    a_star_search(args[3])


if __name__ == '__main__':
    main(sys.argv)
