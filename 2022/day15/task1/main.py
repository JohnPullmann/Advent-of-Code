import os
import math

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


def exclusion_zone(inp: list = [str]) -> int:
    """There is set of sensors and beacons, on input you get location of sensor and location of beacon,
    between sensor and nearest beacon can't be any beacons - area without beacons,
    you need to return area without beacon on specific row"""

    sensors = []
    devices_on_testing_y = set()
    testing_y = 2000000
    # process input
    for line in inp:
        parts = line.split(" ")
        Sx, Sy = int(parts[2].split('=')[1].replace(',', '')), int(parts[3].split('=')[1].replace(':', '')) 
        Bx, By = int(parts[8].split('=')[1].replace(',', '')), int(parts[9].split('=')[1].replace(',', ''))
        if Sy == testing_y:
            devices_on_testing_y.add(Sx)
        if By == testing_y:
            devices_on_testing_y.add(Bx)

        sensor = (Sx, Sy, ( abs(Sx-Bx) + abs(Sy-By) ))
        sensors.append(sensor)

    
    absent_positions = set()
    for sensor in sensors:
        radius = sensor[2] - abs(sensor[1]-testing_y)
        
        if radius >= 0:

            for p in range(sensor[0]-radius, sensor[0]+radius+1):
                absent_positions.add(p)

    return len(absent_positions - devices_on_testing_y)


if __name__ == "__main__":
    inp = load_input()
    if inp != -1:
        result = exclusion_zone(inp)
    print(result)