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


def rucksack_reorg(inp: list = [str]) -> int:
    """find common item in two halfs of rucksack and return sum of it's priorities"""
    common_items = []
    for rucksack in inp:
        rucksack = [ord(x)+(-96 if ord(x) > 97 else -38) for x in rucksack]
        rucksack1 =  rucksack[:round(len(rucksack)/2)]
        rucksack2 =  rucksack[round(len(rucksack)/2):]
        common_item = list(set(rucksack1).intersection(rucksack2))[0]
        common_items.append(common_item)
    return sum(common_items)


if __name__ == "__main__":
    inp = load_input()
    if inp != -1:
        result = rucksack_reorg(inp)
    print(result)