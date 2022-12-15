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


def tuning_trouble(inp: list = [str]) -> int:
    """find first sequence of four unique characters in a row and return index of sequence"""
    sequence = ""
    for i, char in enumerate(inp[0]):
        sequence += char
        if len(sequence) > 4:
            sequence = sequence[1:]
            if len(set(sequence)) == 4:
                return i+1


if __name__ == "__main__":
    inp = load_input()
    if inp != -1:
        result = tuning_trouble(inp)
    print(result)