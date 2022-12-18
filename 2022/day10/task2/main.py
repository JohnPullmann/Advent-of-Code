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


def cathode_ray_tube(inp: list = [str]):
    """You get list of executed instructions, 'noop' instruction just takes one cycle and does nothing,
    'addx' takes two cycles and changes register, signal strength is cycle * register,
    you need to return sum of signal strengths at cycles - 20, 60, ...
    """
    class CPU:
        def __init__(self):
            self.X = 1
            self.cycle_n = 0
            self.memory = {}
            
        def cycle(self):
            self.cycle_n += 1
            self.memory[self.cycle_n] = self.X

            if self.cycle_n%40-1 in [self.X-1, self.X, self.X+1]:
                print('#', end='')
            else:
                print('.', end='')
            if self.cycle_n%40 == 0:
                print('\n', end='')
        
        def addx(self, x: int):
            self.cycle()
            self.cycle()
            self.X += x
        
        def test(self, c: int) -> int:
            print(f"{self.memory[c]*c} - {c}: {self.memory[c]}")
            return self.memory[c]*c


    tests = [20,60,100,140,180,220]
    cpu = CPU()

    for line in inp:
        command, *args = line.split(" ")
        
        if command == "noop":
            cpu.cycle()

        elif command == "addx":
            arg = int(args[0])
            cpu.addx(arg)
        


if __name__ == "__main__":
    inp = load_input()
    if inp != -1:
        cathode_ray_tube(inp)