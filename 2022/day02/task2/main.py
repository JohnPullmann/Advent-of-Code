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
        pl1, result = match.split(" ")
        choice_score_draw = {"A": 1, "B": 2, "C": 3}
        choice_score_lose = {"A": 3, "B": 1, "C": 2}
        choice_score_win = {"A": 2, "B": 3, "C": 1}
        if result == "Z": # You need to win
            scores.append(6+choice_score_win[pl1])
        elif result == "Y": # You need Draw
            scores.append(3+choice_score_draw[pl1])
        else: # You need to lose
            scores.append(choice_score_lose[pl1])
            
    return scores


if __name__ == "__main__":
    inp = load_input()
    if inp != -1:
        scores = matches_to_scores(inp)
        result = sum(scores)
    print(result)