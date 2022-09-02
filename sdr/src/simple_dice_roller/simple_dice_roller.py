from random import randint
import re, argparse
# set up the Die class
class Die():
    def __init__(self,size):
        self.size = int(size[1:])
    def roll(self):
        result = randint(1,self.size)
        return result
#
def roll(args):
    inp = args.roll[0]
    if ',' in inp:
        inp_list = [re.sub(' ','',i) for i in inp.split(',')]
    elif ',' not in inp:
        inp_list = [re.sub(' ','',inp)]
    # perform the actual rolls
    results = []
    for item in inp_list:
        matches = re.search('(.*)x(.*)',item)
        num = int(matches.group(1))
        dice = matches.group(2)
        for i in range(num):
            die = Die(dice)
            results.append(die.roll())
    print(sum(results))
#
def results(args):
    inp = args.results[0]
    if ',' in inp:
        inp_list = [re.sub(' ','',i) for i in inp.split(',')]
    elif ',' not in inp:
        inp_list = [re.sub(' ','',inp)]
    # perform the actual rolls
    results = {}
    for item in inp_list:
        matches = re.search('(.*)x(.*)',item)
        num = int(matches.group(1))
        dice = matches.group(2)
        for i in range(num):
            die = Die(dice)
            roll = die.roll()
            if not f'{dice}-{roll}' in results.keys():
                results[f'{dice}-{roll}'] = 1
            elif f'{dice}-{roll}' in results.keys():
                results[f'{dice}-{roll}'] += 1
    for i in sorted(results.keys()):
        print(f'{i}: {results[i]}')
def main():
    parser = argparse.ArgumentParser(description = "A die-/dice-rolling program")
    #
    parser.add_argument("roll", nargs = '*', metavar = "num", type = str, help = "Enter how many and what type of dice to roll, and the total will be printed. Formatting example:\nEnter '1xd4,2xd6,4xd8,8xd10,16xd12,32xd20' for one 4-sided die,\ntwo 6-sided dice, four 8-sided dice, eight 10-sided dice,\nsixteen 12-sided dice, and thirty two 20-sided dice.")
    parser.add_argument("-l","--results", nargs = '*', metavar = "num", type = str, help = "Print results instead of total.")
    #
    args = parser.parse_args()
    #
    if len(args.roll) > 0:
        try:
            roll(args)
        except Exception as e:
            print(str(e))

    elif args.results != None:
        results(args)
#
if __name__ == "__main__":
    # calling the main function
    main()