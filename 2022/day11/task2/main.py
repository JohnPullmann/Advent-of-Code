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


def middle_monkey(inp: list = [str]) -> int:
    """Monkeys are playing with items and throwing them to other monkeys,
    You need to return 'monkey business' - the busiest monkey times second busiest monkey"""

    class Monkey():
        monkeys_lcm = None
        monkeys = []
        def __init__(self, idM: int, items: list[int], operation: list[str], test: list[str], result_true: int, result_false: int):
            self.idM = idM
            self.items = items
            self.result_true = result_true
            self.result_false = result_false
            self.activity = 0
            # process str to operation
            if '+' in operation:
                self.operation = lambda a: a + (int(operation[4]) if operation[4][0].isdigit() else a)
            elif '*' in operation:
                self.operation = lambda a: a * (int(operation[4]) if operation[4][0].isdigit() else a)
            # process str to test
            self.test = lambda a: a % int(test[2]) == 0
            self.devisor = int(test[2])

            Monkey.monkeys.append(self)

        def __repr__(self):
            return f"{__class__.__name__}({self.idM}, {self.items})"
        
        @staticmethod
        def round():
            for m  in monkeys:
                for item in m.items.copy():
                    i_item = m.items.index(item)
                    #monkey inspects item
                    m.items[i_item] = m.operation(m.items[i_item])                 
                    m.activity += 1
                    #test
                    t = m.test(m.items[i_item])
                    m.items[i_item] = Monkey.monkeys_lcm + m.items[i_item]%Monkey.monkeys_lcm
                    if t:
                        des_monkey = m.result_true
                    else:
                        des_monkey = m.result_false
                    #move item to monkey
                    monkeys[des_monkey].items.append(m.items.pop(i_item))
        
        @staticmethod
        def set_lcm():
            devisors = [m.devisor for m in Monkey.monkeys]
            Monkey.monkeys_lcm = math.lcm(*devisors)


    monkeys = []
    items = operation = test = result_true = result_false = None

    #create monkeys from input
    for line in inp:
        if line == '':
            monkeys.append(Monkey(idM, items, operation, test, result_true, result_false))
        else:
            parts = line.split(" ")
            if line[0] == 'M':
                idM = int(parts[1][:-1])
            elif line[2] == 'S':
                items = [int(item[:].replace(",", "")) for item in parts[4:]]
            elif line[2] == 'O':
                operation = parts[3:]
            elif line[2] == 'T':
                test = parts[3:]
            elif line[7] == 't':
                result_true = int(parts[9])
            elif line[7] == 'f':
                result_false = int(parts[9])
    monkeys.append(Monkey(idM, items, operation, test, result_true, result_false))
    Monkey.set_lcm()

    #run rounds
    for i in range(1,10001):
        Monkey.round()
        #if i in [1,20,1000,2000,3000,4000,5000,6000,7000,8000,9000,10000]:
        #    print(f"== After round {i} ==")
        #    for m in monkeys:
        #        #print(f"Moneky {m.idM}: {m.items}")
        #        print(f"Monkey {m.idM} inspected items {m.activity} times.")
        
    
    monkey_activities = [m.activity for m in monkeys]
    monkey_activities.sort()
    b1, b2 = monkey_activities.pop(), monkey_activities.pop()

    return b1 * b2



if __name__ == "__main__":
    inp = load_input()
    if inp != -1:
        result = middle_monkey(inp)
    print(result)