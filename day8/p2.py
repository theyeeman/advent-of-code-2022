import time


def _score_look_up(matrix, i, j):
    curr_height = matrix[i][j]
    row = i - 1
    score = 0

    while row >= 0:
        if matrix[row][j] < curr_height:
            score += 1
            row -= 1
        else:
            score += 1
            break

    return score


def _score_look_down(matrix, i, j):
    curr_height = matrix[i][j]
    row = i + 1
    score = 0

    while row < len(matrix):
        if matrix[row][j] < curr_height:
            score += 1
            row += 1
        else:
            score += 1
            break

    return score


def _score_look_left(matrix, i, j):
    curr_height = matrix[i][j]
    col = j - 1
    score = 0

    while col >= 0:
        if matrix[i][col] < curr_height:
            score += 1
            col -= 1
        else:
            score += 1
            break

    return score


def _score_look_right(matrix, i, j):
    curr_height = matrix[i][j]
    col = j + 1
    score = 0

    while col < len(matrix[0]):
        if matrix[i][col] < curr_height:
            score += 1
            col += 1
        else:
            score += 1
            break

    return score


def get_scenic_score(matrix, i, j):

    return (
        _score_look_down(matrix, i, j)
        * _score_look_up(matrix, i, j)
        * _score_look_left(matrix, i, j)
        * _score_look_right(matrix, i, j)
    )


def main():
    matrix = standard_func.get_input_as_str('input.txt')
    # matrix = standard_func.get_input_as_str('test.txt')

    curr_max = 0
    
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            curr_max = max(curr_max, get_scenic_score(matrix, i, j))


    print(curr_max)


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
