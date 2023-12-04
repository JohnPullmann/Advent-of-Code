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
    """Find the sum of all numbers in the matrix that are not adjacent to a symbol"""
    matrix = [list(line) for line in inp]
    around = [(-1, -1), (-1, 0), (-1, 1), (0, -1),
              (0, 1), (1, -1), (1, 0), (1, 1)]

    def find_whole_number(x, y, matrix, numbers) -> str:
        """find whole number in line"""
        matrix[x][y] = '~'
        if y-1 >= 0:
            if matrix[x][y-1].isdigit():
                numbers.insert(0, matrix[x][y-1])
                matrix, numbers = find_whole_number(x, y-1, matrix, numbers)
        if y+1 < len(matrix):
            if matrix[x][y+1].isdigit():
                numbers.append(matrix[x][y+1])
                matrix, numbers = find_whole_number(x, y+1, matrix, numbers)

        return [matrix, numbers]

    # find symbols and numbers around them
    numbers = []
    for y,line in enumerate(matrix):
        for x, c in enumerate(line):
            if not c.isdigit() and c != '.':
                for dx, dy in around:
                    if 0 <= x + dx < len(line) and 0 <= y + dy < len(matrix):
                        if matrix[y + dy][x + dx].isdigit():
                            
                            matrix, nums= find_whole_number(y + dy, x + dx, matrix, [matrix[y + dy][x + dx]])
                            nums = int("".join(nums))
                            numbers.append(nums)

    #print("\n".join(["".join(line)for line in matrix]))
    return sum(numbers)

if __name__ == "__main__":
    inp = load_input()
    if inp != -1:
        result = day03(inp)
    print(result)