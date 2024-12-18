def main():
    print(count_xmas_in_grid('./day_four_input.txt'))

def count_xmas_in_grid(file_path):
    def find_xmas(grid, word):
        n = len(grid)
        count = 0
        word_len = len(word)

        # Check diagonally and reversed diagonally
        for d in range(-n + 1, n):
            diag1 = ''.join(grid[i][i - d] for i in range(max(d, 0), min(n + d, n)))
            diag2 = ''.join(grid[i][n - 1 - i + d] for i in range(max(d, 0), min(n + d, n)))
            count += diag1.count(word) + diag1[::-1].count(word)
            # Check for X-shaped "MAS"
            for d in range(-n + 2, n - 1):
                for i in range(max(d, 0), min(n + d, n) - 2):
                    if (grid[i][i - d] == 'M' and grid[i + 1][i + 1 - d] == 'A' and grid[i + 2][i + 2 - d] == 'S' and
                        grid[i][n - 1 - i + d] == 'S' and grid[i + 1][n - 2 - i + d] == 'A' and grid[i + 2][n - 3 - i + d] == 'M'):
                        count += 1
                    if (grid[i][i - d] == 'S' and grid[i + 1][i + 1 - d] == 'A' and grid[i + 2][i + 2 - d] == 'M' and
                        grid[i][n - 1 - i + d] == 'M' and grid[i + 1][n - 2 - i + d] == 'A' and grid[i + 2][n - 3 - i + d] == 'S'):
                        count += 1

        return count

    with open(file_path, 'r') as file:
        grid = [list(line.strip()) for line in file.readlines()]

    return find_xmas(grid, "XMAS")

if __name__ == '__main__':
    main()