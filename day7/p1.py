import time


def _get_ls_output(inputs, i):
    ls_output = []

    while i < len(inputs) and not _is_command(inputs[i]):
        ls_output.append(inputs[i])
        i += 1
    
    return ls_output


def parse_input_into_dict(inputs):
    history = []
    d = {}
    curr = d

    for i, row in enumerate(inputs):
        if _is_cd_dir(row):
            history.append(curr)
            curr = curr[_get_cd_dir(row)]
        elif _is_cd_dotdot(row):
            curr = history.pop()
        elif _is_ls(row):
            objects = _get_ls_output(inputs, i+1)

            for object in objects:
                if _is_file(object):
                    curr.setdefault(_get_file_name(object), _get_file_size(object))
                else:
                    curr.setdefault(_get_directory_name(object), {})
        else:
            continue

    return d


def _is_directory(line):
    return line.split(' ')[0] == 'dir'


def _get_directory_name(line):
    return line.split(' ')[1]


def _is_file(line):
    return not _is_directory(line)


def _get_file_name(line):
    return line.split(' ')[1]


def _get_file_size(line):
    return int(line.split(' ')[0])


def _is_command(line):
    return line.split(' ')[0] == '$'


def _is_cd(line):
    return _is_command(line) and line.split(' ')[1] == 'cd'


def _is_cd_dotdot(line):
    return _is_cd(line) and line.split(' ')[2] == '..'


def _get_cd_dir(line):
    return line.split(' ')[2]


def _is_cd_dir(line):
    return _is_cd(line) and line.split(' ')[2] != '..'


def _is_ls(line):
    return _is_command(line) and line.split(' ')[1] == 'ls'


def is_directory(value):
    return type(value) is dict


def is_file(value):
    return type(value) is int


def get_all_directory_sums(d, all_sums):
    curr_sum = 0

    for value in d.values():
        if is_directory(value):
            curr_sum += get_all_directory_sums(value, all_sums)
        else:
            curr_sum += value

    all_sums.append(curr_sum)
    return curr_sum


def main():
    inputs = standard_func.get_input_as_str('input.txt')[1:]
    # inputs = standard_func.get_input_as_str('test.txt')[1:]  # trim first line since it is root
    
    d = parse_input_into_dict(inputs)
    all_sums = []

    get_all_directory_sums(d, all_sums)
    print(sum([val if val <= 100000 else 0 for val in all_sums]))

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
