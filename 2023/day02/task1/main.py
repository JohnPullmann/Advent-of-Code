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


def day02(inp: list = [str]) -> int:
    """"""
    result = 0
    for line in inp:
        impossible = False
        gameID = int(line.split(":")[0].split(" ")[1])
        sets = {index: {x.strip().split(" ")[1]: int(x.strip().split(" ")[0]) for x in value.strip().split(",")} for index, value in enumerate(line.split(":")[1].split(";")) } 
        for cube_set in sets.values():
            if "red" in cube_set:
                if cube_set["red"] > 12:
                    impossible = True
                    break
            if "green" in cube_set:
                if cube_set["green"] > 13:
                    impossible = True
                    break
            if "blue" in cube_set:
                if cube_set["blue"] > 14:
                    impossible = True
                    break
        if not impossible:
            result += gameID
    return result

    


if __name__ == "__main__":
    inp = load_input()
    if inp != -1:
        result = day02(inp)
    print(result)