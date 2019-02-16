#test_game_of_life

import Game_of_life

def test_matrix():
    assert Game_of_life.matrix(0, 5, 5) == [[0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0]]

def test_initial_matrix():
    assert Game_of_life.initial_matrix(1, [[0, 0, 0],[1, 1, 1], [0, 0, 0]]
) == [[0, 0, 0],[1, 1, 1], [0, 0, 0]]


    
    
    
