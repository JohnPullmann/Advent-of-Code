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


def camp_cleanup(inp: list = [str]) -> int:
    """return number of cases when one range contains other"""
    contain_pair = 0
    for pair in inp:
        r1, r2 = [r.split('-') for r in pair.split(",")]
        r1 = set(range(int(r1[0]),int(r1[1])+1))
        r2 = set(range(int(r2[0]),int(r2[1])+1))
        if r1.issubset(r2) or r2.issubset(r1):
            contain_pair += 1

    return contain_pair


if __name__ == "__main__":
    inp = load_input()
    if inp != -1:
        result = camp_cleanup(inp)
    print(result)