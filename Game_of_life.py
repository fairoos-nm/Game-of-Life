#Game_of_life

def matrix(element, row, column):
    matrix_out = [[element] * row for i in range(column)]
    return matrix_out
