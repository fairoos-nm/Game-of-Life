 #Game_of_life


def neighbours1(matrix1,position):
    for sub_list in matrix1:
        for j in range(len(matrix1)):
            for i in range(len(sub_list)):
                my_pos = [j, i]
                if my_pos == position:
                    neighbours_list = [[j-1, i-1], [j-1, i], [j-1, i+1], [j, i-1], [j, i+1],[j+1, i-1],[j+1, i],[j+1, i+1]]
                    
                    return  neighbours_list

def neighbours(matrix1):
    for sub_list in matrix1:
        for j in range(len(matrix1)):
            for i in range(len(sub_list)):
                my_pos = [j, i]
                neighbours_list = [[j-1, i-1], [j-1, i], [j-1, i+1], [j, i-1], [j, i+1],[j+1, i-1],[j+1, i],[j+1, i+1]]
                    
                return  neighbours_list

def real_neighbours(neighbours_list):
    a = []
    for neighbour in neighbours_list:
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
            neib = real_neighbours(neighbours1(metrix, position))
            for a in neib:
                x = a[0]
                y = a[1]
                f = metrix[x]
                n = f[y]
                if n  == 1:
                    count = count + 1        
            result[i][j] = count
    return result

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
                
def display(board):
    row = len(board)
    column =  len(board[0])
    a = ""
    for i in range(row):
        for j in range(column):
            if j == 0:
                a += "\n"
            if board[i][j] == 1:
                a += "0 "
            if board[i][j] == 0:
                a += ". "
            
    return a
    
