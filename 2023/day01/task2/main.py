import os
import regex as re



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


def day01(inp: list = [str]) -> int:
    """Filter out non-digit characters and sum the values and spelled numbers also count as numbers"""
    numbers = "(^a(?=\s)|one|two|three|four|five|six|seven|eight|nine|ten| \
          eleven|twelve|thirteen|fourteen|fifteen|sixteen|seventeen| \
          eighteen|nineteen|twenty|thirty|forty|fifty|sixty|seventy|eighty| \
          ninety|hundred|thousand|[0-9]+)"
    result_numbers = []
    for line in inp:
        filtered = re.findall(numbers, line, overlapped=True)

        # map text numbers to digits
        text_to_num = {"zero": "0", "one": "1", "two": "2", "three": "3", "four": "4", "five": "5", "six": "6", "seven": "7", "eight": "8", "nine": "9", "ten": "10", "eleven": "11", "twelve": "12", "thirteen": "13", "fourteen": "14", "fifteen": "15", "sixteen": "16", "seventeen": "17", "eighteen": "18", "nineteen": "19", "twenty": "20", "thirty": "30", "forty": "40", "fifty": "50", "sixty": "60", "seventy": "70", "eighty": "80", "ninety": "90", "hundred": "00", "thousand": "000"}
        converted = []
        for element in filtered:
            if not element.isdigit():
                converted.append(text_to_num[element])
            else:
                if len(element) == 1:
                    converted.append(element)
                else:
                    for e in element:
                        converted.append(e)
                    
        first_and_last = int(converted[0]+converted[-1])
        result_numbers.append(first_and_last)

    return sum(result_numbers)


if __name__ == "__main__":
    inp = load_input()
    if inp != -1:
        result = day01(inp)
    print(result)