import helper


def main():
    return


def calculate_valid_ordering():
    ordering = []
    with open("./day_five_input.txt", "r") as file:
        lines = file.readlines()
        for line in lines:
            numbers = line.split(",")
            include_into_ordering(numbers, ordering)
    return ordering

def include_into_ordering(numbers, ordering):
    for number in numbers:
        number = number.strip()
        if number not in ordering:
            ordering.append(number)
        else:
            index = ordering.index(number)
    return ordering