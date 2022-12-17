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
    """find place with best view and return number of visible trees from that place"""
    trees = []
    for line in inp:
        trees.append([int(tree) for tree in line])
    scenic_score = [[0 for tree in line] for line in trees]


    for y in range(1,len(trees)-1):
        for x in range(1, len(trees[0])-1):
            t = trees[y][x]
            
            left = 0
            for i in [tree for tree in trees[y][:x]][::-1]:
                if t > i:
                    left += 1
                else:
                    left +=1
                    break
            
            right = 0
            for i in [tree for tree in trees[y][x+1:]]:
                if t > i:
                    right += 1
                else:
                    right +=1
                    break

            up = 0
            for i in [line[x] for line in trees[:y]][::-1]:
                if t > i:
                    up += 1
                else:
                    up +=1
                    break

            down = 0
            for i in [line[x] for line in trees[y+1:]]:
                if t > i:
                    down += 1
                else:
                    down +=1
                    break
            scenic_score[y][x] = left * right * up * down

    best_place = max([max(line) for line in scenic_score])
    return best_place


if __name__ == "__main__":
    inp = load_input()
    if inp != -1:
        result = treetop_tree_house(inp)
    print(result)