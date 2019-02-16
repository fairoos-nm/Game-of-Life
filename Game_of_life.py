#Game_of_life

def matrix(element, row, column):
    matrix_out = [[element] * row for i in range(column)]
    return matrix_out

a =1
matrix1 = [[0, 0, 0],[1, 1, 1], [0, 0, 0]]

def initial_matrix(a, matrix1):
    for sub_list in matrix1:
        if matrix1[1] == sub_list:
            for i in sub_list:
                sub_list[i] = 1
                return matrix1

        
