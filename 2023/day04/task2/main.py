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
    """Play cards until you run out of cards and return number of played cards"""
    global cards
    cards_winnnigs = {}
    n_of_cards = {x+1:1 for x in range(len(inp))}
    out_of_cards = {x+1:0 for x in range(len(inp))}
    cards_n = 0

    def card_winning(line):
        #extract winning numbers
        winning_numbers = [n for n in line.split(":")[1].split("|")[0].split(' ') if n != '']
        #extract your numbers and select only numbers in winning numbers
        my_winning_numbers = [n for n in line.split(":")[1].split("|")[1].split(' ') if n in winning_numbers]
        # return number of winning numbers
        return len(my_winning_numbers)

    # find out how many winning numbers are in each card
    for i, line in enumerate(inp):
        cards_winnnigs[i+1] = card_winning(line)

    # play cards until you run out of cards
    while True:
        # play cards based on number of winning numbers of cards
        for card_id, n_of_card in n_of_cards.items():
            if n_of_card:
                cards_n += 1
                for i in range(card_id+1, card_id+cards_winnnigs[card_id]+1):
                    n_of_cards[i] += 1
                n_of_cards[card_id] -= 1
        # check if all types of cards are out of cards
        if n_of_cards == out_of_cards:
            break

    return cards_n

if __name__ == "__main__":
    inp = load_input()
    if inp != -1:
        result = day04(inp)
    print(result)