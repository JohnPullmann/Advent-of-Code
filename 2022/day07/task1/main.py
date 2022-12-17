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


class dir:
    def __init__(self, name, parent=None):
        self.name = name
        self.parent = parent
        self.content = {}
        self.__dirs_under_100KB = []

    @property
    def size(self):
        return sum([x.size for x in self.content.values()])

    @property
    def dirs_under_100KB(self):
        self.size

        # find dirs under 100KB
        self.__dirs_under_100KB = []
        for d in self.content.values():
            if isinstance(d, dir):
                self.__dirs_under_100KB.extend(d.dirs_under_100KB)  
                if d.size < 100000:
                    self.__dirs_under_100KB.append(d)

        return list(set(self.__dirs_under_100KB))

    def __repr__(self):
        return f"{self.__class__.__name__}({self.name}, {self.size})"


class file:
    def __init__(self, name, size):
        self.name = name
        self.size = size
    
    def __repr__(self):
        return f"{self.__class__.__name__}({self.name}, {self.size})"

class commands():
    @staticmethod
    def move_to_root(root):
        return root
    
    @staticmethod
    def move_back(current_dir):
        return current_dir.parent

    @staticmethod
    def move_to_folder(current_dir, folder_name):
        return current_dir.content[folder_name]
    
    @staticmethod
    def ls(current_dir, index, inp):
        current_dir.content = {}
        for line in inp[index+1:]:
            if line[0] != '$':
                p1, p2 = line.split(' ')
                if line[0] == 'd':
                    current_dir.content[p2] = dir(name=p2, parent=current_dir)
                else:
                    current_dir.content[p2] = file(name=p2, size=int(p1))
            else:
                break


def no_space_left_on_device(inp: list = [str]) -> int:
    """return sum of dirs under 100000 based on commands and outputs from input"""
    root = dir(name='/')
    current_dir = root

    for i, line in enumerate(inp):
        if line[0] == '$':
            dollar, command, *arguments = line.split()
            if command == "ls":
                commands.ls(current_dir, i, inp)
            if command == "cd":
                if arguments[0] == "..":
                    current_dir = commands.move_back(current_dir)
                elif arguments[0] == '/':
                    current_dir = commands.move_to_root(root)
                else:
                    current_dir = commands.move_to_folder(current_dir, arguments[0])

    return sum([x.size for x in root.dirs_under_100KB])




if __name__ == "__main__":
    inp = load_input()
    if inp != -1:
        result = no_space_left_on_device(inp)
    print(result)