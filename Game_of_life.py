#Game_of_life

def matrix(element, row, column):
    matrix_out = [[element] * row for i in range(column)]
    return matrix_out

#a =1
#matrix1 = [[0, 0, 0],[1, 1, 1], [0, 0, 0]]

def initial_matrix(a, matrix1):
    for sub_list in matrix1:
        if matrix1[1] == sub_list:
            for i in sub_list:
                sub_list[i] = 1
                return matrix1


def neighbours( matrix1, position):
    for sub_list in matrix1:
        for j in range(len(matrix1)):
            for i in range(len(sub_list)):
                my_pos = [j, i]
                if my_pos == position:
                     neighbours_list = [[j-1, i-1], [j-1, i], [j-1, i+1], [j, i-1], [j, j+1],[j+1, i-1],[j+1, i],[j+1, i+1]]
                     return neighbours_list

def real_neighbours(neighbours_list):
    a = []
    for neighbor in neighbours_list:
        for x in neighbor:
            if x < 0 or x > 2:
                neighbor.remove(x)
        a.append(neighbor)
        for i in a:
            if len(i) == 1:
                a.remove(i)
    return a
    
     

def position_of_alive_elements(initial_matrix):
    alive = 1
    position = []
    j = 0
    for x in initial_matrix:
        i = 0
        for y in x:
            if y == 1:
                position.append([j, i])
            i = i + 1
        j = j + 1
    return position                  

def apply_rules(initial_stage, positions):
    alive = 1
    dead = 0
    posi = []
    for 1st_position in positions:
        for j in range(len(initial_stage)):
            for i in range(len(row)):
                print [j, i]
                if [j, i] == 1st_posi:
                   for row in initial_stage:
                       
        
    
    
    


def main():
    row = 3
    column = 3
    element = 0
    1st_matrix = matrix(element, row, column)
    a = 1
    initial_stage = initial_matrix(a, 1st_matrix)
    positions = position_of_alive_elements(initial_stage)
    all_neighbors = neighbours( initial_stage, position)
    neighbors = real_neighbours(all_neighbors)
    
