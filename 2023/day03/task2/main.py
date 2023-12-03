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
    """ Find gears with two adjacent numbers and multiply numbers and sum gears"""
    matrix = [list(line) for line in inp]
    around = [(-1, -1), (-1, 0), (-1, 1), (0, -1),
              (0, 1), (1, -1), (1, 0), (1, 1)]

    def find_whole_number(x, y, matrix, numbers) -> str:
        """find whole number in line"""
        matrix[x][y] = '.'
        if y-1 >= 0:
            if matrix[x][y-1].isdigit():
                numbers.insert(0, matrix[x][y-1])
                matrix, numbers = find_whole_number(x, y-1, matrix, numbers)
        if y+1 < len(matrix):
            if matrix[x][y+1].isdigit():
                numbers.append(matrix[x][y+1])
                matrix, numbers = find_whole_number(x, y+1, matrix, numbers)

        return [matrix, numbers]


    gears = {}
    for y,line in enumerate(matrix):
        for x, c in enumerate(line):
            if c == '*':
                if (x,y) not in gears:
                    gears[(x,y)] = []
                for dx, dy in around:
                    if 0 <= x + dx < len(line) and 0 <= y + dy < len(matrix):
                        if matrix[y + dy][x + dx].isdigit():
                            
                            matrix, numbers = find_whole_number(y + dy, x + dx, matrix, [matrix[y + dy][x + dx]])
                            
                            gears[(x,y)].append(int("".join(numbers)))
    result = 0
    for gear in gears:
        if len(gears[gear]) == 2:
            result += gears[gear][0] * gears[gear][1]

    return result



if __name__ == "__main__":
    inp = load_input()
    if inp != -1:
        result = day03(inp)
    print(result)