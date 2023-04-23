# Written by Devin M. Gardner of Railway Signal Systems, 12-11-2022
# Intended for IXS and EC5 signalling systems, for converting vital configuration switch settings to hex equivalent
# This was mainly for fun. We have a macro-enabled Excel sheet that's done this since 2016, but I wanted to create something CLI for it.
# I also know there are libraries to make this far easier, and that I really made this painstakingly difficult for myself, but I'm not really that concerned with efficiency on this tool.
# I'll likely make a GUI version as well.
#
# set up an empty list
settings = []
# define a function to continually ask for True or False until one is provided, to ensure all bits are handled
def get_answer(i):
    answer = input(f'Is Vital Setting {i} True or False?\n> ')
    # if the answer isn't 'True' or 'False', print an error message and then call the function again
    if answer != 'True' and answer != 'False':
        print(f'Please enter True or False.')
        get_answer(i)
    # return 'True' or 'False'
    return answer
# iterate through 1-32, asking for True or False and adding it to the list
for i in range(1,33):
    settings.append(get_answer(i))
# list comprehension to go through the list and replace 'True' with 1 and 'False' with 0, and then make it one long number
settings = ''.join(['1' if i == 'True' else '0' for i in settings])
# create an empty list to group up 4 bits at a time
groups = []
# while the settings variable still contains characters, grab up to index 4 (non-inclusive) and append it to the 'groups' list as one string, and then update 'settings' to only contain from index 4 (inclusive) onwards
while len(settings) > 0:
    groups.append(settings[:4])
    settings = settings[4:]
# define a function to convert a 4-bit word (in the form of a 4-character string) into its decimal counterpart
def bin_to_hex(inp):
    total = 0
    # split the string into a list of 4 characters
    inp = list(inp)
    # enumerate the reversed copy of the input string
    for ind,i in enumerate(reversed(inp)):
        exp = 2 ** ind
        if i == '1':
            total += exp
        else:
            continue
    return total
# iterate through the groups, converting each one to hexadecimal
answer = []
for group in groups:
    answer.append(bin_to_hex(group))
# set up another dictionary for the hexadecimal values and their decimal counterparts
hex = '0123456789ABCDEF'
hex_dict = {}
for ind,i in enumerate(hex):
    hex_dict[ind] = i
# go through the 'answer' variable and compare to the hex_dict
final_answer = []
for i in answer:
    final_answer.append(hex_dict[i])
final_answer = ''.join(final_answer)
print(f'The hex equivalent of the settings you entered is <{final_answer}>')