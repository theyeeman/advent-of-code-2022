import time


CHECKPOINTS = [20, 60, 100, 140, 180, 220]


def main():
    inputs = standard_func.get_input_as_str('input.txt')
    # inputs = standard_func.get_input_as_str('test.txt')
    cycle_count = 1
    signal_strength = 0
    x = 1

    for input in inputs:
        instruction = input.split(' ')
        print(instruction)

        if cycle_count in CHECKPOINTS:
            CHECKPOINTS.remove(cycle_count)
            print(cycle_count, x)
            signal_strength += cycle_count * x
        
        if instruction[0] == 'noop':
            cycle_count += 1
            if cycle_count in CHECKPOINTS:
                CHECKPOINTS.remove(cycle_count)
                print(cycle_count, x)
                signal_strength += cycle_count * x
        else:
            value = int(instruction[1])
            cycle_count += 1

            if cycle_count in CHECKPOINTS:
                CHECKPOINTS.remove(cycle_count)
                print(cycle_count, x)
                signal_strength += cycle_count * x

            print(f'cycle_count: {cycle_count}, x: {x}')
    
            x += value
            cycle_count += 1

            if cycle_count in CHECKPOINTS:
                CHECKPOINTS.remove(cycle_count)
                print(cycle_count, x)
                signal_strength += cycle_count * x

        print(f'cycle_count: {cycle_count}, x: {x}')

    print(signal_strength)


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
