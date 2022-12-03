import time


PRIORITY = {
    'a': 1,
    'b': 2,
    'c': 3,
    'd': 4,
    'e': 5,
    'f': 6,
    'g': 7,
    'h': 8,
    'i': 9,
    'j': 10,
    'k': 11,
    'l': 12,
    'm': 13,
    'n': 14,
    'o': 15,
    'p': 16,
    'q': 17,
    'r': 18,
    's': 19,
    't': 20,
    'u': 21,
    'v': 22,
    'w': 23,
    'x': 24,
    'y': 25,
    'z': 26,
    'A': 27,
    'B': 28,
    'C': 29,
    'D': 30,
    'E': 31,
    'F': 32,
    'G': 33,
    'H': 34,
    'I': 35,
    'J': 36,
    'K': 37,
    'L': 38,
    'M': 39,
    'N': 40,
    'O': 41,
    'P': 42,
    'Q': 43,
    'R': 44,
    'S': 45,
    'T': 46,
    'U': 47,
    'V': 48,
    'W': 49,
    'X': 50,
    'Y': 51,
    'Z': 52,
}


def _split_in_half(row):
    return [row[:len(row)//2], row[len(row)//2:]]


def parse_input_into_rucksacks(inputs):
    return [_split_in_half(row) for row in inputs]


def get_priority(letter):
    return PRIORITY[letter]


def get_same_letter_in_rucksack(rucksack):
    # It seems like there is only ever 1 intersection between the compartments (i.e. there will not be >1 letters matched between categories)
    return set(rucksack[0]).intersection(set(rucksack[1])).pop()


def main():
    inputs = standard_func.get_input_as_str('input.txt')
    # inputs = standard_func.get_input_as_str('test.txt')
    rucksacks = parse_input_into_rucksacks(inputs)
    priority_sum = 0

    for rucksack in rucksacks:
        same_letter = get_same_letter_in_rucksack(rucksack)
        priority_sum += get_priority(same_letter)

    print(priority_sum)


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
