# this code is wrong since the rope moves incorrectly, but at least it has a cool visualization
# the problem is that i am assuming that each knot in the rope must go into the previous knot's position, 
# but that is not necessarily true
import time
import os

class Node:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def copy(self):
        return Node(self.x, self.y)

    def move_once(self, direction):
        if direction == 'L':
            self.x -= 1
        elif direction == 'R':
            self.x += 1
        elif direction == 'U':
            self.y += 1
        elif direction == 'D':
            self.y -= 1

    def __repr__(self) -> str:
        return f'x: {self.x}, y: {self.y}'


def is_diagonal(n1, n2):
    return n1.x != n2.x and n1.y != n2.y


def calc_distance(n1, n2):  # manhattan distance
        return abs(n1.x - n2.x) + abs(n1.y - n2.y)


def parse_move(move):
    splitted = move.split(' ')
    return splitted[0], int(splitted[1])    


def debug_pretty_print(matrix):
    print('*************************')
    for row in matrix[::-1]:
        print(''.join(row))
    print('*************************')


def debug_grid(body, tail_spaces=None):
    matrix = [['.' for q in range(20)] for _ in range(20)]

    for i in range(len(body)-1, -1, -1):
        matrix[body[i].y][body[i].x] = str(i)

    if tail_spaces:
        for space in tail_spaces:
            matrix[space[1]][space[0]] = ' '

    debug_pretty_print(matrix)


def main():
    os.system('cls' if os.name == 'nt' else 'clear')
    # inputs = standard_func.get_input_as_str('input.txt')
    inputs = standard_func.get_input_as_str('test.txt')
    tail_spaces = set()
    body = [Node(0, 0) for _ in range(10)]  # body[0] will be head

    for row in inputs:
        direction, magnitude = parse_move(row)

        for _ in range(magnitude):
            tail_spaces.add((body[-1].x, body[-1].y))
            prev_body = [node.copy() for node in body]
            body[0].move_once(direction)

            for i in range(len(body)-1):
                head = body[i]
                tail = body[i+1]

                if is_diagonal(head, tail):
                    if calc_distance(head, tail) >= 3:
                        body[i+1] = prev_body[i].copy()
                else:
                    if calc_distance(head, tail) >= 2:
                        body[i+1] = prev_body[i].copy()

            os.system('cls' if os.name == 'nt' else 'clear')
            print(f'direction: {direction}, magnitude: {magnitude}')
            tail_spaces.add((body[-1].x, body[-1].y))
            debug_grid(body)
            print(tail_spaces)
            time.sleep(0.1)


    # print(tail_spaces)
    print(len(tail_spaces))
    

# Boilerplate code below
class standard_func:
    def get_input_as_int(filename):
        with open(filename) as f:
            return list(map(lambda a : int(a), list((f.read()).split("\n"))))

    def get_input_as_str(filename):
        with open(filename) as f:
            return list((f.read()).split("\n"))

    def print_performance(start, end):
        print('Execution time (s):', round((end - start), 3))


if __name__ == "__main__":
    perf_counter_start = time.perf_counter()
    main()
    perf_counter_end = time.perf_counter()
    standard_func.print_performance(perf_counter_start, perf_counter_end)
