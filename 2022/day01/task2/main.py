import os

def load_input() -> list[str]:
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


def get_max_cal(inp: list = []) -> int:
    # sum calories for each elf and return sum of first three elfs
    elfs_cal = []
    elf_cal = 0
    for line in inp:
        if line == '':
            elfs_cal.append(elf_cal)
            elf_cal = 0
        else:
            try:
                elf_cal += int(line)
            except ValueError:
                print("Invalid input!")
                return -1

    if elfs_cal != []:
        elfs_cal.sort(reverse=True)
        if len(elfs_cal) > 3:
            return sum([elfs_cal[0],elfs_cal[1],elfs_cal[2]])
        else:
            return sum(elfs_cal)
    else:
        print("Input is empty!")
        return -1


if __name__ == "__main__":
    inp = load_input()
    if inp != -1:
        result = get_max_cal(inp)
    print(result)