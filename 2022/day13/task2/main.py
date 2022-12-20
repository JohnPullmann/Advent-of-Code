import os
import json
from functools import cmp_to_key

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


def distress_signal(inp: list = [str]) -> int:
    """compare pairs of lists and return sum of indexes of pairs that were in right order based on specific criterias"""
    def compare_lists(list1, list2) -> bool:
        l_list1 = len(list1)
        l_list2 = len(list2)
        for i in range(min([l_list1, l_list2])):
            e_list1 = list1[i]
            e_list2 = list2[i]
            if isinstance(e_list1, int) and isinstance(e_list2, int):
                if e_list1 < e_list2:
                    return 1
                elif e_list1 == e_list2:
                    continue
                else:
                    return -1
            elif isinstance(e_list1, list) and isinstance(e_list2, int) or isinstance(e_list1, int) and isinstance(e_list2, list):
                if isinstance(e_list1, int):
                    e_list1 = [e_list1]
                else:
                    e_list2 = [e_list2]
            if isinstance(e_list1, list) and isinstance(e_list2, list):
                r =  compare_lists(e_list1, e_list2)
                if r == 0:
                    continue
                else:
                    return r
        
        if l_list1 < l_list2:
            return 1
        elif l_list1 == l_list2:
            return 0
        else:
            return -1

    packets = []
    for line in inp:
        if line != "":
            packets.append(json.loads(line))
    packets.append([[2]])
    packets.append([[6]])

    packets = sorted(packets, key=cmp_to_key(lambda l1, l2: compare_lists(l1, l2)), reverse=True)
    
    return (packets.index([[2]])+1) * (packets.index([[6]])+1)
            

if __name__ == "__main__":
    inp = load_input()
    if inp != -1:
        result = distress_signal(inp)
    print(result)