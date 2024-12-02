def main():
    
    safeness_counter = 0
    
    input = read_input()
    for line in input:
        numbers = line.split()
        if safeness_check(numbers):
            safeness_counter += 1
    print(f"Number of safe lines: {safeness_counter}")


        

def read_input():
    with open("./day_two_input.txt", "r") as file:
        return file.readlines()


def safeness_check(list):
    delta_min = 1
    delta_max = 3
    if len(list) == 0:
        return True
    for i in range(len(list)-1):
        if abs(list[i] - list[i+1]) < delta_min or abs(list[i] - list[i+1]) > delta_max:
            return False
    return True


if __name__ == "__main__":
    main()