import os

def load_input() -> list[str]:
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


def matches_to_scores(inp: list = [str]) -> list[int]:
    scores = []
    for match in inp:
        pl1, pl2 = match.split(" ")
        cases = {"AX":4,"AY":8,"AZ":3,
                 "BX":1,"BY":5,"BZ":9,
                 "CX":7,"CY":2,"CZ":6,
        }

        scores.append(cases[pl1+pl2])
    return scores


if __name__ == "__main__":
    inp = load_input()
    if inp != -1:
        scores = matches_to_scores(inp)
        result = sum(scores)
    print(result)