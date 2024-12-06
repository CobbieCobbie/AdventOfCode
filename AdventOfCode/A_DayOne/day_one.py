def main():
    input = read_input()
    list1 = []
    list2 = []
    for line in input:
        numbers = line.split()
        list1.append(int(numbers[0]))
        list2.append(int(numbers[1]))

    result = 0

    list1.sort()
    list2.sort()


    for i in range(len(list1)):
        print(str(result))
        result += compare(list1[i],list2[i])

    print(f"the result is now {result}")
    similarity = similarity_score(list1, list2)
    print(f"The similarity score is {similarity}")


def similarity_score(list1, list2):
    similarity = 0
    for i in range(len(list1)):
        occurrence = 0
        for j in range(len(list1)):
            if list1[i] == list2[j]: 
                occurrence += 1
        similarity += (list1[i] * occurrence)
    return similarity


def read_input():
    with open("./day_one_input.txt", "r") as file:
        return file.readlines()

def compare(i, j):
    return abs(i-j)


def list_check(list1, list2):
    if not len(list1) == len(list2):
        return False
    for l in list1:
        if not isinstance(l, int):
            return False
    for l in list2:
        if not isinstance(l, int):
            return False
    return True
    
    
if __name__ == '__main__':
    main()