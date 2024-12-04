class IndexAndDirection:
    def __init__(self, a, b, c, d):
        self.a = a
        self.b = b
        self.c = c
        self.d = d

def is_in_bounds(matrix, i, j):
    return 0 <= i < len(matrix) and 0 <= j < len(matrix[i])

def check_cell_is_char(matrix, line, column, char):
    if is_in_bounds(matrix, line, column) and matrix[line][column] == char:
        return True

def check_cross(matrix, line, column, char):
    to_return = 0
    if is_in_bounds(matrix, line, column + 2) and matrix[line][column + 2] == char:
        # M - M
        # - A -
        # S - S
        # OR
        # S - S
        # - A -
        # M - M
        if (check_cell_is_char(matrix, line+1, column+1, 'A') and check_cell_is_char(matrix, line+2, column+2, 'S') and check_cell_is_char(matrix, line+2, column, 'S')):
            to_return += 1
        if (check_cell_is_char(matrix, line-1, column+1, 'A') and check_cell_is_char(matrix, line-2, column+2, 'S') and check_cell_is_char(matrix, line-2, column, 'S')):
            to_return += 1
    if is_in_bounds(matrix, line + 2, column) and matrix[line + 2][column] == char:
        # M - S
        # - A -
        # M - S
        # OR
        # S - M
        # - A -
        # S - M        
        if (check_cell_is_char(matrix, line+1, column+1, 'A') and check_cell_is_char(matrix, line+2, column+2, 'S') and check_cell_is_char(matrix, line, column+2, 'S')):
            to_return += 1
        if (check_cell_is_char(matrix, line+1, column-1, 'A') and check_cell_is_char(matrix, line+2, column-2, 'S') and check_cell_is_char(matrix, line, column-2, 'S')):
            to_return += 1
    return to_return
        



with open("input", "r") as file:
    matrix = [list(line.strip()) for line in file.readlines()]

total = 0

for i in range(len(matrix)):
    for j in range(len(matrix[i])):
        if matrix[i][j] == 'M':
            total += check_cross(matrix, i, j, 'M')

print(total)