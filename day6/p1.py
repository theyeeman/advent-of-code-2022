# This code was serverely rushed in an attempt to get onto the leaderboard
import time


def is_four_unique_letters(letters):
    if len(set(letters)) < 4:
        return False

    return True


def main():
    # inputs = standard_func.get_input_as_str('input.txt')
    input = standard_func.get_input_as_str('input.txt')[0]

    for i in range(0, len(input)-4):
        if is_four_unique_letters(input[i:i+4]):
            print(i + 4)
            break


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
