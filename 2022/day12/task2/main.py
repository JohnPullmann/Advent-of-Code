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


def hill_climbing(inp: list = [str]) -> int:
    """Climb a hill and return fewest steps required to move from any lowest position to destination"""
    class board:
        board = []
        layers = {}
        active_layer = 0
        starting_cells = []
        ending_cell = None
        ending_cells = []
        shortest_path_found = False
    
        def round(self) -> bool:
            board.layers[board.active_layer+1] = []

            for c in board.layers[board.active_layer]:
                c.find_accessible_neighbours()

            board.active_layer += 1
            
            return board.shortest_path_found

        def print_board(self, what_to_print: str = "id"):
            for line in board.board:
                for c in line:
                    if what_to_print == "id":
                        print(c.id, end="")
                    elif what_to_print == "cost":
                        print(c.cost, end="")
                print(" ")


    class cell(board):
        def __init__(self, id: str, x: int, y: int):
            self.cost = None
            self.id = id
            self.height = ord(id)
            self.neighbours = []
            self.x = x
            self.y = y
            self.path = []

            if id == 'E':
                board.starting_cell = self
                board.layers[0] = [self]
                self.cost = 0
                self.height = ord('z')
            elif id == 'a':
                board.ending_cells.append(self)

            
        def find_accessible_neighbours(self):
            dirs = [[-1,0], [1,0], [0,-1], [0,1]]
            for d in dirs:
                n_cell_pos = (self.x+d[0], self.y+d[1])
                if 0 <= n_cell_pos[0] < len(board.board[0]) and 0 <= n_cell_pos[1] < len(board.board):
                    n_cell = board.board[n_cell_pos[1]][n_cell_pos[0]]
                    if n_cell.cost == None and n_cell.height+1 >= self.height:
                        self.neighbours.append(n_cell)
                        board.layers[board.active_layer+1].append(n_cell)
                        n_cell.cost = board.active_layer+1
                        n_cell.path = self.path.copy()
                        n_cell.path.append(self)

                        if n_cell.id == 'a':
                            board.ending_cell = n_cell
                            board.shortest_path_found = True


        def __repr__(self):
            return f"{__class__.__name__}({self.id}, {self.height}, {(self.x, self.y)})"

    Board = board()
    # process input
    board.board = [[cell(c, x, y) for x, c in enumerate(line)] for y, line in enumerate(inp)]

    found = False
    while not found:
        found = Board.round()


    return Board.active_layer


if __name__ == "__main__":
    inp = load_input()
    if inp != -1:
        result = hill_climbing(inp)
    print(result)