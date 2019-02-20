 # #Game_of_life

# row = 3
# column = 3
# element = 0
# def matrix(element, row, column):
#     matrix_out = [[element] * row for i in range(column)]
#     return matrix_out

# first_matrix = (matrix(element, row, column))

# print (first_matrix)

# def initial_matrix(position, matrix1):
#     for row_no in range(len(matrix1)):
#         if row_no == 1:
#             matrix1[1] = [1, 1, 1]
#     return matrix1

# initial_stage = initial_matrix(first_matrix)
# print(initial_stage)

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


def neighbours( matrix1, position):
    for sub_list in matrix1:
        for j in range(len(matrix1)):
            for i in range(len(sub_list)):
                my_pos = [j, i]
                if my_pos == position:
                    neighbours_list = [[j-1, i-1], [j-1, i], [j-1, i+1], [j, i-1], [j, i+1],[j+1, i-1],[j+1, i],[j+1, i+1]]
                    
                    return  neighbours_list


                 
def real_neighbours(neighbours_list):
    a = []
    for neighbour in neighbours_list:
        # print (neighbour)
        for x in neighbour:
            if x < 0 or x > 2:
                neighbour.remove(x)
        a.append(neighbour)
        for i in a:
            if len(i) == 1:
                a.remove(i)
    return a



def count_alive_neighbours(metrix):
    
    rows = len(metrix)
    cols = len(metrix[0])
    result = [[None for i in range(cols)] for j in range(rows)]
    
    for i in range(len(metrix)):
        for j in range(len(metrix[0])):
            position = [i,j]
            count = 0
            neib = real_neighbours(neighbours(metrix, position))
            for a in neib:
                x = a[0]
                y = a[1]
                #print (a, x, y)
                f = metrix[x]
                #print(f)
                n = f[y]
                #print(n)
                if n  == 1:
                    count = count + 1        
            result[i][j] = count
    return result





metrix = [[0, 0, 0], [1, 1, 1], [0, 0 , 0]]

alive_list = count_alive_neighbours(metrix)

def apply_rules(alive_list, metrix):
    
    rows = len(metrix)
    columns = len(metrix[0])    
    for i in range(rows):
        for j in range(columns):
            if metrix[i][j]:
                if alive_list[i][j] < 2 or  alive_list[i][j] > 3:
                    metrix[i][j] = 0
            if metrix[i][j]:
                if alive_list[i][j] == 3 or alive_list[i][j] == 2:
                    metrix[i][j] = 1

            if metrix[i][j] == 0 and alive_list[i][j] == 3:
                metrix[i][j] =1
    return metrix
                
    
print(apply_rules(alive_list,metrix))    
    

# def main():

    
    
#     print
#     positions = position_of_alive_elements(initial_stage)
#     all_neighbors = neighbours( initial_stage, position)
#     neighbors = real_neighbours(all_neighbors)
#     print(neighbours)
