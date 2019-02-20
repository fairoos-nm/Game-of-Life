import Game_of_life
import time

def main():
    matrix = [[0, 1, 0],[0, 1, 0],[0, 1, 0]]
    while True:
        total_neighbours = Game_of_life.neighbours(matrix)
        real_neib = Game_of_life.real_neighbours(total_neighbours)
        living_nib = Game_of_life.count_alive_neighbours(matrix)
        ruled_matrix = Game_of_life.apply_rules(living_nib, matrix)
        print(Game_of_life.display(ruled_matrix))
        time.sleep(.5)
    
main()
