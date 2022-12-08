import time


def _can_look_up(matrix, i, j):
    curr_height = matrix[i][j]
    row = i - 1

    while row >= 0:
        if matrix[row][j] >= curr_height:
            return False

        row -= 1

    return True


def _can_look_down(matrix, i, j):
    curr_height = matrix[i][j]
    row = i + 1

    while row < len(matrix):
        if matrix[row][j] >= curr_height:
            return False

        row += 1

    return True


def _can_look_left(matrix, i, j):
    curr_height = matrix[i][j]
    col = j - 1

    while col >= 0:
        if matrix[i][col] >= curr_height:
            return False

        col -= 1

    return True


def _can_look_right(matrix, i, j):
    curr_height = matrix[i][j]
    col = j + 1

    while col < len(matrix[0]):
        if matrix[i][col] >= curr_height:
            return False

        col += 1

    return True


def is_tree_visible(matrix, i, j):

    return (
        _can_look_down(matrix, i, j)
        or _can_look_up(matrix, i, j)
        or _can_look_left(matrix, i, j)
        or _can_look_right(matrix, i, j)
    )


def main():
    matrix = standard_func.get_input_as_str('input.txt')
    # matrix = standard_func.get_input_as_str('test.txt')

    inner_trees = 0
    
    for i in range(1, len(matrix)-1):
        for j in range(1, len(matrix[0])-1):
            if is_tree_visible(matrix, i, j):
                inner_trees += 1

    print(inner_trees + 2 * (len(matrix) + len(matrix[0])) - 4)


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
