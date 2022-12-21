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


def regolith_reservoir(inp: list = [str]) -> int:
    """You get coords of lines of rock in 2D grid, sand is falling from point (500, 0) and comming to rest,
    find number of units of send come to rest until they start to fall into void"""
    solid_points = []
    source = (500, 500)
    for line in inp:
        line_points = 0
        line_points = [[int(x)for x in x.split(",")] for x in line.split("->")]
        for l in range(len(line_points)-1):
            if line_points[l][0] < line_points[l+1][0]+1:
                for x in range(line_points[l][0], line_points[l+1][0]+1):
                    if line_points[l][1] < line_points[l+1][1]+1:
                        for y in range(line_points[l][1], line_points[l+1][1]+1):
                            if (x,y) not in solid_points:
                                solid_points.append((x,y))
                    else:
                        for y in range(line_points[l+1][1], line_points[l][1]+1):
                            if (x,y) not in solid_points:
                                solid_points.append((x,y))

            else:
                for x in range(line_points[l+1][0], line_points[l][0]+1):
                    if line_points[l][1] < line_points[l+1][1]+1:
                        for y in range(line_points[l][1], line_points[l+1][1]+1):
                            if (x,y) not in solid_points:
                                solid_points.append((x,y))
                    else:
                        for y in range(line_points[l+1][1], line_points[l][1]+1):
                            if (x,y) not in solid_points:
                                solid_points.append((x,y))

    #print(len(solid_points))
    lowest_point_y = max([p[1] for p in solid_points])
    #print(f"lowest point {lowest_point_y}")
    stop = False
    n_sand = 0
    while not stop:
        sand = (500,0)
        while True:
            if (sand[0],sand[1]+1) not in solid_points:
                if sand[1]+1 > lowest_point_y:
                    stop = True
                    break
                sand = (sand[0],sand[1]+1)
            elif (sand[0]-1,sand[1]+1) not in solid_points:
                sand = (sand[0]-1,sand[1]+1)
            elif (sand[0]+1,sand[1]+1) not in solid_points:
                sand = (sand[0]+1,sand[1]+1)
            else:
                solid_points.append(sand)
                n_sand += 1
                break
    return n_sand



if __name__ == "__main__":
    inp = load_input()
    if inp != -1:
        result = regolith_reservoir(inp)
    print(result)