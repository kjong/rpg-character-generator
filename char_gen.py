#!/usr/bin/python

import random
from collections import OrderedDict

# creates number to base character on
def gen_char_num(in_name) -> int:
    random.seed(in_name)
    # generate 16 digit char_num
    return "%0.16d" % random.randint(0,9999999999999999)

# gets portion of char_num from index i to j
def slice_char_num(char_num, i, j) -> int:
    if i == j:
        return int(str(char_num[i]))
    else:
        return int((str(char_num)[i:j]).lstrip("0"))

# gets line at index of file
def get_line_at_index(filename, char_num, i, j) -> str:
    f = open(filename)
    lines = f.readlines()
    count = len(lines)
    line = lines[slice_char_num(char_num, i, j) % count - 1].rstrip()
    f.close()

    return line

# rolls character attributes based on char_num
def gen_char(in_name, char_num):
    char_dict = OrderedDict()

    # name
    char_dict["name"] = in_name

    # surname (4 numbers)
    char_dict["surname"] = get_line_at_index("surnames.txt", char_num, 0, 4).capitalize()

    # race (2 numbers)
    char_dict["race"] = get_line_at_index("races.txt", char_num, 4, 6).capitalize()

    # cosmic force (1 number)
    char_dict["cosmic force"] = get_line_at_index("cosmic_forces.txt", char_num, 6, 6)

    # alignment (1 number)
    char_dict["alignment"] = get_line_at_index("alignment_chart.txt", char_num, 7, 7)

    # strength (1 number)
    if str(char_num)[8] == str(0):
        char_dict["strength"] = str(1)
    else:
        char_dict["strength"] = str(char_num)[8]

    # agility (1 number)
    if str(char_num)[9] == str(0):
        char_dict["agility"] = str(1)
    else:
        char_dict["agility"] = str(char_num)[9]

    # intelligence (1 number)
    if str(char_num)[10] == str(0):
        char_dict["intelligence"] = str(1)
    else:
        char_dict["intelligence"] = str(char_num)[10]

    # charisma (1 number)
    if str(char_num)[11] == str(0):
        char_dict["charisma"] = str(1)
    else:
        char_dict["charisma"] = str(char_num)[11]

    # weapon type (2 numbers)
    char_dict["weapon"] = get_line_at_index("weapons.txt", char_num, 12, 14)

    # utility item (2 numbers)
    char_dict["utility item"] = get_line_at_index("utility_items.txt", char_num, 14, 16)

    return char_dict

# prints generated character
def print_char(char_dict):
    print(char_dict.get("name") + " the " + char_dict.get("surname"))

    new_dict = list(char_dict.items())
    new_dict = dict(new_dict[2:])
    for att in new_dict:
        print("Your " + str(att) + " is: " + new_dict[att])

# main
def main():
    print("Enter your name: ")
    in_name = input()
    
    char_num = gen_char_num(in_name.replace(" ", ""))    
    char_dict = gen_char(in_name, char_num)

    print_char(char_dict)    

if __name__ == "__main__":
    main()
