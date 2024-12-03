from functools import reduce
from operator import mul

import re


def main():
    print("First result", calc_part_one(read_input()))
    print("Second result", calc_part_two(read_input()))

def calc_part_one(input):
    pattern = get_regex_one()
    result = 0
    for line in input:
        muls = re.findall(pattern, line)
        for mul in muls:
            result += eval(mul)
    return result

def calc_part_two(input):
    pattern_one = get_regex_one()
    pattern_two = get_regex_two()
    result = 0
    for line in input:
        muls = re.findall(pattern_one, line)
        mul_one = muls[0]
        result += eval(mul_one)
    for line in input:
        do_muls = re.findall(pattern_two, line)
        print(do_muls)
        for d in do_muls:
            result += calc_part_one(do_muls)
    return result

def read_input():
    with open("./day_three_input.txt", "r") as file:
        return file.readlines()

def get_regex_one():
    return r'mul\(\d{1,3},\d{1,3}\)'

def get_regex_two():
    return r'do\(\).*?mul\(\d{1,3},\d{1,3}\)'

def eval(str):
    numbers = re.findall(r'\d+', str)
    return reduce(mul,list(map(int, numbers)))


if __name__ == '__main__':
    main()

