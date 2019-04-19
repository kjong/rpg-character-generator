#!/usr/bin/python

import random

# gets portion of char_num from index i to j
def slice_char_num(char_num, i, j) -> int:
    return int((str(char_num)[i:j]).lstrip("0"))

# creates number to base character on
def gen_char_num(in_name) -> int:
    random.seed(in_name)
    # generate 10 digit char_num
    return "%0.12d" % random.randint(0,999999999999)\

# rolls character attributes based on char_num
def gen_char(in_name, char_num) -> dict:
    char_dict = {}

    # name
    char_dict["name"] = in_name

    # surname (4 numbers)
    f = open("surnames.txt")
    lines = f.readlines()
    count = len(lines)
    char_dict["surname"] = lines[slice_char_num(char_num, 0, 4) % count - 1].rstrip()
    f.close()

    # # strength (1 number)
    char_dict["str"] = str(char_num)[4]

    # # agility (1 number)
    char_dict["agi"] = str(char_num)[5]

    # # intelligence (1 number)
    char_dict["int"] = str(char_num)[6]

    # weapon type (2 numbers)
    f = open("weapon_types.txt")
    lines = f.readlines()
    count = len(lines)
    print(slice_char_num(char_num, 7, 9))
    print(slice_char_num(char_num, 7, 9) % count - 1)
    print(lines[slice_char_num(char_num, 7, 9) % count - 1])
    char_dict["weapon"] = lines[slice_char_num(char_num, 7, 9) % count - 1].rstrip()
    f.close()

    # cosmic force alignment ()


    return char_dict

# #
# def print_char(char_dict):


# main
def main():
    print("Enter your name: ")
    in_name = input()
    char_num = gen_char_num(in_name.replace(" ", ""))    
    char_dict = gen_char(in_name, char_num)

    print("Your character number is: " + str(char_num))
    for att in char_dict:
        print("Your " + str(att) + " is: " + char_dict[att])

if __name__ == "__main__":
    main()
