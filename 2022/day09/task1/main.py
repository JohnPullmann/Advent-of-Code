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


def rope_bridge(inp: list = [str]) -> int:
    """Head is moving around and tail is following head when distance between them is greater than 1
    Return number of unique places they visit
    """
    visited_places = {(0,0)}
    head, tail, last_head = (0,0), (0,0), (0,0)

    for line in inp:
        d, n = line.split(" ")

        for _ in range(int(n)):
            last_head = head
            if d == 'R':
                head = (head[0]+1,head[1])
            elif d == 'L':
                head = (head[0]-1,head[1])
            elif d == 'U':
                head = (head[0],head[1]-1)
            else:
                head = (head[0],head[1]+1)
            
            if abs(head[0]-tail[0]) >= 2 or abs(head[1]-tail[1]) >= 2:
                tail = last_head
                visited_places.add(tail)
        
    return len(visited_places)



if __name__ == "__main__":
    inp = load_input()
    if inp != -1:
        result = rope_bridge(inp)
    print(result)