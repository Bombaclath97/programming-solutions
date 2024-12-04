class IndexAndDirection:
    def __init__(self, a, b, c, d):
        self.a = a
        self.b = b
        self.c = c
        self.d = d

def is_in_bounds(matrix, i, j):
    return 0 <= i < len(matrix) and 0 <= j < len(matrix[i])

def check_cell_is_char(matrix, line, column, char, direction_i, direction_j):
    nline, ncolumn =  direction_i + line, direction_j + column
    if is_in_bounds(matrix, nline, ncolumn) and matrix[nline][ncolumn] == char:
        return True

def check_neighbor_is_char(matrix, line, column, char):
    to_return = []
    for i, j in [(-1, 0), (1, 0), (0, -1), (0, 1), (1, 1), (-1, -1), (1, -1), (-1, 1)]:
        nline, ncolumn =  i + line, j + column
        if is_in_bounds(matrix, nline, ncolumn) and matrix[nline][ncolumn] == char:
            to_return.append(IndexAndDirection(nline, ncolumn, i, j))
    return to_return


with open("input", "r") as file:
    matrix = [list(line.strip()) for line in file.readlines()]

total = 0

for i in range(len(matrix)):
    for j in range(len(matrix[i])):
        if matrix[i][j] == 'X':
            m_neighbors = check_neighbor_is_char(matrix, i, j, 'M')
            if len(m_neighbors) > 0:
                for m in m_neighbors:
                    m_i, m_j, d_i, d_j = m.a, m.b, m.c, m.d
                    if check_cell_is_char(matrix, m_i, m_j, 'A', d_i, d_j) and check_cell_is_char(matrix, m_i + d_i, m_j + d_j, 'S', d_i, d_j):
                        total += 1
            else:
                continue

print(total)