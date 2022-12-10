import time
import os

CHECKPOINTS = [20, 60, 100, 140, 180, 220]


def draw_on_crt(crt, cycle, x):
    modulo_cycle = cycle % 40
    print(f'crt cycle: {cycle}, modulo_cycle: {modulo_cycle}, x: {x}')

    if modulo_cycle >= x-1 and modulo_cycle <= x+1:
        print(f'drawing on position {cycle}')
        crt[cycle] = '#'


def print_crt(crt):
    # crt = crt[1:]
    for i in range(6):
        print(''.join(crt[i*40:i*40 + 40]))


def main():
    os.system('cls')
    inputs = standard_func.get_input_as_str('input.txt')
    # inputs = standard_func.get_input_as_str('test.txt')
    cycle_count = 0
    x = 1
    crt = ['.' for _ in range(241)]

    for input in inputs:
        instruction = input.split(' ')
        print(f'instruction: {instruction}')
        print(f'before: cycle_count: {cycle_count}, x: {x}')

        draw_on_crt(crt, cycle_count, x)
        
        if instruction[0] == 'noop':
            cycle_count += 1
            draw_on_crt(crt, cycle_count, x)

        else:
            value = int(instruction[1])
            cycle_count += 1

            draw_on_crt(crt, cycle_count, x)

            x += value
            cycle_count += 1

            draw_on_crt(crt, cycle_count, x)
        
        print(f'after: cycle_count: {cycle_count}, x: {x}')

    print_crt(crt)


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
