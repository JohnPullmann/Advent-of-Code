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
        self.__dirs_to_delete = []

    @property
    def size(self):
        return sum([x.size for x in self.content.values()])

    @property
    def dirs_to_delete(self):
        self.size

        # find potential dirs to delete
        self.__dirs_to_delete = []
        for d in self.content.values():
            if isinstance(d, dir):
                self.__dirs_to_delete.append(d)
                self.__dirs_to_delete.extend(d.dirs_to_delete)  
                    

        return list(set(self.__dirs_to_delete))

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

    free_space = (70000000-root.size)
    needed_space = 30000000 - free_space
    dirs_enough = []
    for d in root.dirs_to_delete:
        if d.size > needed_space:
            dirs_enough.append(d.size)

    return min(dirs_enough)




if __name__ == "__main__":
    inp = load_input()
    if inp != -1:
        result = no_space_left_on_device(inp)
    print(result)