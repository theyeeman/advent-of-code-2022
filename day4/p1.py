import time


def has_complete_overlap(first, second):
    if first[0] >= second[0] and first[1] <= second[1] or second[0] >= first[0] and second[1] <= first[1]:
        return True

    return False


def parse_input(inputs):
    ret = []

    for input in inputs:
        temp = input.split(',')
        pair1 = [int(c) for c in temp[0].split('-')]
        pair2 = [int(c) for c in temp[1].split('-')]
        ret.append([pair1, pair2])

    return ret


def main():
    inputs = standard_func.get_input_as_str('input.txt')
    # inputs = standard_func.get_input_as_str('test.txt')

    parsed = parse_input(inputs)
    count = 0

    for parse in parsed:
        if has_complete_overlap(parse[0], parse[1]):
            count += 1

    print(count)
    

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
