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

position = [1, 1]

def neighbours( matrix1, position):
    for sub_list in matrix1:
        for j in range(len(matrix1)):
            for i in range(len(sub_list)):
                my_pos = [j, i]
                if my_pos == position:
                     neighbours_list = [[j-1, i-1], [j-1, i], [j-1, i+1], [j, i-1], [j, j+1],[j+1, i-1],[j+1, i],[j+1, i+1]]
                     return neighbours_list
                    
 
