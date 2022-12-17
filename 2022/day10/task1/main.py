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


def cathode_ray_tube(inp: list = [str]) -> int:
    """You get list of executed instructions, 'noop' instruction just takes one cycle and does nothing,
    'addx' takes two cycles and changes register, signal strength is cycle * register,
    you need to return sum of signal strengths at cycles - 20, 60, ...
    """
    tests = [20,60,100,140,180,220]
    memory = {}
    X = 1
    cycle = 0
    for line in inp:
        command, *args = line.split(" ")
        
        if command == "noop":
            cycle += 1
            memory[cycle] = X
        elif command == "addx":
            arg = int(args[0])
            for _ in range(2):
                cycle += 1
                memory[cycle] = X
            X += arg

    return sum([memory[x]*x for x in tests])


if __name__ == "__main__":
    inp = load_input()
    if inp != -1:
        result = cathode_ray_tube(inp)
    print(result)