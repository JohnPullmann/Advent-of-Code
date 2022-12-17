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


def treetop_tree_house(inp: list = [str]) -> int:
    """return number of visible trees in forest"""
    trees = []
    for line in inp:
        trees.append([int(tree) for tree in line])
    visible = [[False for tree in line] for line in trees]

    # mark all trees on edge as visible
    visible[0] = visible[-1] = [True for _ in range(len(trees[0]))]
    for i in range(len(trees)):
        visible[i][0] = visible[i][-1] = True

    # mark all other visible trees
    for y in range(1,len(trees)-1):
        for x in range(1, len(trees[0])-1):
            t = trees[y][x]
            left = True if t > max([tree for tree in trees[y][:x]]) else False # left
            right = True if t > max([tree for tree in trees[y][x+1:]]) else False # right
            up = True if t > max([line[x] for line in trees[:y]]) else False # up
            down = True if t > max([line[x] for line in trees[y+1:]]) else False # down
            visible[y][x] = left or right or up or down

    visible_trees = sum([line.count(True) for line in visible])
    return visible_trees


if __name__ == "__main__":
    inp = load_input()
    if inp != -1:
        result = treetop_tree_house(inp)
    print(result)