import re


def main():
    pattern = r'mul\(\d{1,3},\d{1,3}\)'
    if re.fullmatch(pattern, "mul(1,3)"):
        print("Matched")


if __name__ == '__main__':
    main()
