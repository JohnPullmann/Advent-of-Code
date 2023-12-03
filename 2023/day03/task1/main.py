import os
from pprint import pprint

def load_input() -> list[str]:
    """read input.txt file for task input and return list of lines of input"""
    # Read and return text input from input.txt
    try:
        dirname = os.path.dirname(__file__)
        path_to_input = os.path.join(dirname, 'input.txt')
        with open(path_to_input, 'r') as file:
            inp = file.read().splitlines()
    except FileNotFoundError:
        print("File input.txt was not found!")
        return -1
    return inp


def day03(inp: list = [str]) -> int:
    """ Find the sum of all numbers in the matrix that are not adjacent to a symbol"""
    matrix = [list(line) for line in inp]
    around = [(-1, -1), (-1, 0), (-1, 1), (0, -1),
              (0, 1), (1, -1), (1, 0), (1, 1)]

    def remove_adjacent_numbers(x, y, matrix) -> str:
        """remove adjacent numbers from string"""
        if y-1 >= 0:
            if matrix[x][y-1].isdigit():
                matrix[x][y-1] = '.'
                matrix = remove_adjacent_numbers(x, y-1, matrix)
        if y+1 < len(matrix):
            if matrix[x][y+1].isdigit():
                matrix[x][y+1] = '.'
                matrix = remove_adjacent_numbers(x, y+1, matrix)

        return matrix

    # change all non digits to dots
    matrix_copy = [[c if c.isdigit() else '.' for c in line] for line in matrix if line]
    # get all numbers in matrix
    part = 0
    for i,line in enumerate(matrix_copy):
        matrix_copy[i] = "".join(line).split('.')
        matrix_copy[i] = [int(c) for c in matrix_copy[i] if c]
        part += sum(matrix_copy[i])


    for y,line in enumerate(matrix):
        for x, c in enumerate(line):
            if not c.isdigit() and c != '.':

                for dx, dy in around:
                    if 0 <= x + dx < len(line) and 0 <= y + dy < len(matrix):
                        if matrix[y + dy][x + dx].isdigit():
                            matrix[y + dy][x + dx] = '.'
                            matrix = remove_adjacent_numbers(y + dy, x + dx, matrix)


    # change all non digits to dots
    matrix = [[c if c.isdigit() else '.' for c in line] for line in matrix if line]
    # get all numbers in matrix
    non_part = 0
    for i,line in enumerate(matrix):
        matrix[i] = "".join(line).split('.')
        matrix[i] = [int(c) for c in matrix[i] if c]
        non_part += sum(matrix[i])

    return part-non_part



if __name__ == "__main__":
    inp = load_input()
    if inp != -1:
        result = day03(inp)
    print(result)