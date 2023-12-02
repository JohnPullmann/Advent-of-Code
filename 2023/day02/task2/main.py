import os
import math

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


def day02(inp: list = [str]) -> int:
    """Find minimums for each color and multiply them together. Then return the sum of all of these."""
    result = 0
    for line in inp:
        sets = {index: {x.strip().split(" ")[1]: int(x.strip().split(" ")[0]) for x in value.strip().split(",")} for index, value in enumerate(line.split(":")[1].split(";")) } 
        minimums = {"red": 0, "green": 0, "blue": 0}
        for cube_set in sets.values():
            for color in cube_set.keys():
                if cube_set[color] > minimums[color]:
                    minimums[color] = cube_set[color]
        result += math.prod(minimums.values())
    return result

    


if __name__ == "__main__":
    inp = load_input()
    if inp != -1:
        result = day02(inp)
    print(result)