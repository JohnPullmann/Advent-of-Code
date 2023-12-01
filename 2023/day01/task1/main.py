import os

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


def day01(inp: list = [str]) -> int:
    """Filter out non-digit characters and sum the values"""
    lines = ["".join([l for l in line if l.isdigit()]) for line in inp]
    values = [int(line[0]+line[-1]) for line in lines]
    return sum(values)


if __name__ == "__main__":
    inp = load_input()
    if inp != -1:
        result = day01(inp)
    print(result)