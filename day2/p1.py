import time

ROCK_POINTS = 1
PAPER_POINTS = 2
SCISSOR_POINTS = 3

WIN_POINTS = 6
DRAW_POINTS = 3
LOSE_POINTS = 0

# A rock, B paper, C scissors
# X rock, Y paper, Z scissors
POINTS_DICT = {
    'A': {
        'X': DRAW_POINTS + ROCK_POINTS,
        'Y': WIN_POINTS + PAPER_POINTS,
        'Z': LOSE_POINTS + SCISSOR_POINTS,
    },
    'B': {
        'X': LOSE_POINTS + ROCK_POINTS,
        'Y': DRAW_POINTS + PAPER_POINTS,
        'Z': WIN_POINTS + SCISSOR_POINTS,
    },
    'C': {
        'X': WIN_POINTS + ROCK_POINTS,
        'Y': LOSE_POINTS + PAPER_POINTS,
        'Z': DRAW_POINTS + SCISSOR_POINTS,
    },
}


def parse_input(inputs):
    parsed = []

    for row in inputs:
        parsed.append(row.split(' '))

    return parsed


def calc_points(inputs):
    score = 0

    for opponent, me in inputs:
        score += POINTS_DICT[opponent][me]

    return score


def main():
    inputs = standard_func.get_input_as_str('input.txt')
    # inputs = standard_func.get_input_as_str('test.txt')
    parsed_inputs = parse_input(inputs)

    print(calc_points(parsed_inputs))    
    

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
