import time


class Move:
    def __init__(self, quantity, start, end):
        self.quantity = int(quantity)
        self.start = int(start) - 1  # crates are 1-indexed in input
        self.end = int(end) - 1 

    def __repr__(self) -> str:
        return f'quantity: {self.quantity}, start: {self.start}, end: {self.end}'


def _get_moves(inputs):
    move_list = []

    for row in inputs:
        splitted = row.split()
        move_list.append(Move(splitted[1], splitted[3], splitted[5]))

    return move_list


def _get_crate_lists(inputs):
    # parsing the crates will be kind of nasty
    num_crates = int(inputs[-1][-2])
    crates = []

    for crate_num in range(num_crates):
        index = crate_num * 4 + 1
        curr_crates = []

        for row in _reverse(inputs[:-1]):  # do not get last row since it is just crate numbers, go in reverse order so it's bottom to top
            if row[index] == ' ':
                break

            curr_crates.append(row[index])
        
        crates.append(curr_crates)

    return crates


def _reverse(list):
    return list[::-1]


def parse_input(inputs):
    crates = []
    moves = []

    for i, row in enumerate(inputs):
        if row == '':
            moves = inputs[i+1:]
            break

        crates.append(row)

    move_list = _get_moves(moves)
    crate_list = _get_crate_lists(crates)

    return move_list, crate_list


def perform_all_moves(move_list, crate_list):
    for move in move_list:
        start_crate = crate_list[move.start]
        end_crate = crate_list[move.end]

        end_crate += start_crate[len(start_crate) - move.quantity:]
        start_crate = start_crate[:len(start_crate) - move.quantity]

        crate_list[move.start] = start_crate
        crate_list[move.end] = end_crate


def get_top_crates(crate_list):
    return [crate[-1] for crate in crate_list]


def main():
    inputs = standard_func.get_input_as_str('input.txt')
    # inputs = standard_func.get_input_as_str('test.txt')

    move_list, crate_list = parse_input(inputs)
    perform_all_moves(move_list, crate_list)
    print(''.join(get_top_crates(crate_list)))
    

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
