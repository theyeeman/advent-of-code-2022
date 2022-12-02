import time


def get_elf_calories(inputs):
    elf_calories = [0]
    curr_elf = 0

    for row in inputs:
        if row == '':
            elf_calories.append(0)
            curr_elf += 1
        else:
            elf_calories[curr_elf] += int(row)

    return elf_calories


def get_sum_top_n_elf_calories(calories, num_elves):
    calories.sort(reverse=True)

    return sum(calories[:num_elves])


def main():
    inputs = standard_func.get_input_as_str('input.txt')
    # inputs = standard_func.get_input_as_str('test.txt')
    
    elf_calories = get_elf_calories(inputs)

    print(get_sum_top_n_elf_calories(elf_calories, 3))
            

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
