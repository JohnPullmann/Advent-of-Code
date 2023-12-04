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


def day04(inp: list = [str]) -> int:
    """Compare my numbers with winning numbers and get point for based on number of matches and sum points for all cards"""
    result = 0
    for line in inp:
        #extract winning numbers
        winning_numbers = [n for n in line.split(":")[1].split("|")[0].split(' ') if n != '']
        #extract my numbers and select only numbers in winning numbers
        my_winning_numbers = [n for n in line.split(":")[1].split("|")[1].split(' ') if n in winning_numbers]
        # add points for this card
        print(my_winning_numbers,2**(len(my_winning_numbers)-1))
        # add point for this card if there are any my winning numbers
        if len(my_winning_numbers):
            result += 2**(len(my_winning_numbers)-1)
    return int(result)

if __name__ == "__main__":
    inp = load_input()
    if inp != -1:
        result = day04(inp)
    print(result)