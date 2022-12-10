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


def debug_grid(head, tail):
    matrix = [['.' for q in range(10)] for _ in range(10)]
    matrix[tail.y][tail.x] = 'T'
    matrix[head.y][head.x] = 'H'
    debug_pretty_print(matrix)


def main():
    inputs = standard_func.get_input_as_str('input.txt')
    # inputs = standard_func.get_input_as_str('test.txt')
    tail_spaces = set()
    head = Node(0, 0)
    tail = Node(0, 0)

    for row in inputs:
        direction, magnitude = parse_move(row)

        for _ in range(magnitude):
            tail_spaces.add((tail.x, tail.y))
            prev_head = head.copy()
            head.move_once(direction)

            if is_diagonal(head, tail):
                if calc_distance(head, tail) >= 3:
                    tail = prev_head.copy()
            else:
                if calc_distance(head, tail) >= 2:
                    tail = prev_head.copy()

        tail_spaces.add((tail.x, tail.y))

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
