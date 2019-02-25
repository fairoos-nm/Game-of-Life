#test_game_of_life

import Game_of_life


def test_neighbours_of_position():
     assert Game_of_life.neighbours_of_position([[0, 0, 0],[1, 1, 1], [0, 0, 0]], [1, 1]) == [[0, 0], [0, 1], [0, 2], [1, 0], [1, 2], [2, 0], [2, 1], [2, 2]]

    
def test_neighbours():
   
    assert Game_of_life.neighbours([[0, 0, 0],[1, 1, 1], [0, 0, 0]]) == [[-1, -1], [-1, 0], [-1, 1], [0, -1], [0, 1], [1, -1], [1, 0], [1, 1]]


def test_real_neighbours():
    assert Game_of_life.real_neighbours([[-1, -1], [-1, 0], [-1, 1], [0, -1], [0, 1], [1, -1], [1, 0], [1, 1]]) == [[0, 1], [1, 0], [1, 1]]



def test_count_alive_neighbours():
    assert Game_of_life.count_alive_neighbours([[0, 0, 0], [1, 1, 1], [0, 0 , 0]]) == [[2,3,2], [1,2,1], [2,3,2]]

def test_apply_rule():
    alive_list = [[2,3,2], [1,2,1], [2,3,2]]
    metrix = [[0, 0, 0], [1, 1, 1], [0, 0 , 0]]
    assert Game_of_life.apply_rules(alive_list, metrix) == [[0, 1, 0], [0, 1, 0], [0, 1, 0]] 


def test_display():
    matrix1 = [[0, 0, 0], [1, 1, 1], [0, 0 , 0]]
    assert Game_of_life.display(matrix1) == "\n. . . \n0 0 0 \n. . . "
    
    matrix = [[0, 1, 0], [0, 1, 0], [0, 1 , 0]]
    assert Game_of_life.display(matrix) == "\n. 0 . \n. 0 . \n. 0 . "
                                            
