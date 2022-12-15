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
    """find common item of groups of three elfs and return sum of common items"""
    group_elfs = []
    badges = []
    for rucksack in inp:
        rucksack = [ord(x)+(-96 if ord(x) > 97 else -38) for x in rucksack]
        group_elfs.append(rucksack)
        if len(group_elfs) == 3:
            badge = list(set(group_elfs[0]) & set(group_elfs[1]) & set(group_elfs[2]))[0]
            badges.append(badge)
            group_elfs = []

    return sum(badges)


if __name__ == "__main__":
    inp = load_input()
    if inp != -1:
        result = rucksack_reorg(inp)
    print(result)