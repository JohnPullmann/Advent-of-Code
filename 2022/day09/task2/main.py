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
    visited_places = [(0,0)]
    parts = [(0,0),(0,0),(0,0),(0,0),(0,0),(0,0),(0,0),(0,0),(0,0),(0,0)]

    def is_neighbour(point1, point2) -> bool:
        return abs(point1[0]-point2[0]) < 2 and abs(point1[1]-point2[1]) < 2
    
    def move_head(dir):
        if dir == 'R':
            parts[0] = (parts[0][0]+1,parts[0][1])
        elif dir == 'L':
            parts[0] = (parts[0][0]-1,parts[0][1])
        elif dir == 'U':
            parts[0] = (parts[0][0],parts[0][1]-1)
        else:
            parts[0] = (parts[0][0],parts[0][1]+1)
        return parts

    for line in inp:
        dir, n = line.split(" ")

        for _ in range(int(n)):
            parts = move_head(dir)

            for i, part in enumerate(parts):
                if i != 0:
                    if not is_neighbour(parts[i], parts[i-1]):
                        if i == len(parts)-1:
                            visited_places.append(parts[i])

                        # move x 
                        if parts[i][1] == parts[i-1][1]:
                            parts[i] = ((parts[i-1][0]+parts[i][0])//2, parts[i][1])
                            continue
                        # move y
                        if parts[i][0] == parts[i-1][0]:
                            parts[i] = (parts[i][0], (parts[i-1][1]+parts[i][1])//2)
                            continue
                            
                        diags = [[1,1], [-1,-1], [1,-1],[-1,1]]
                        for d in diags:
                            if is_neighbour(parts[i-1], (parts[i][0]+d[0], parts[i][1]+d[1])):
                                parts[i] = (parts[i][0]+d[0], parts[i][1]+d[1])
                                break


    visited_places.append(parts[-1])         
    visited_places = set(visited_places)
    return len(set(visited_places))



if __name__ == "__main__":
    inp = load_input()
    if inp != -1:
        result = rope_bridge(inp)
    print(result)

