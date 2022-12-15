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


def supply_stacks(inp: list = [str]) -> str:
    """return first crates after moving of crates"""
    stacks = []
    line = inp.pop(0)
    #import starting stage of stacks from input
    while line[1] != '1':
        i = line.index("[")+1
        crates = list(line[1::4])
        for i, crate in enumerate(crates):
            if len(stacks) >= i+1:
                if crate != ' ':
                    stacks[i].append(crate)
            else:
                if crate != ' ':
                    stacks.append([crate])
                else:
                    stacks.append([])
        line = inp.pop(0)
    inp.pop(0)

    #move crates
    for move in inp:
        a = move.split(" ")
        n, s, d = int(a[1]), int(a[3])-1, int(a[5])-1
        picked_up = []
        for _ in range(n):
            picked_up.append(stacks[s].pop(0))
            
        stacks[d][0:0] = picked_up

    #get crates on top
    first_crates = ""
    for stack in stacks:
        if stack != []:
            first_crates += stack[0] 
               
    return first_crates


if __name__ == "__main__":
    inp = load_input()
    if inp != -1:
        result = supply_stacks(inp)
    print(result)