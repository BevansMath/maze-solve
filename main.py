from windows import Window
from cell import Cell
from maze import Maze
import sys
# Really hard to debug program that does something different everytime
# Add seed

def main():
    screen_x = 800
    screen_y = 600
    win = Window(screen_x, screen_y)

    num_rows = 12
    num_cols = 16
    margin = 50


    cell_size_x = (screen_x - 2 * margin)/ num_cols
    cell_size_y = (screen_y - 2 * margin) / num_rows
  


    sys.setrecursionlimit(10000)

    maze = Maze(margin, margin, num_rows, num_cols, cell_size_x, cell_size_y, win, 10000)
    
    print("maze created")
    is_solveable = maze.solve()
    if not is_solveable:
        print("Maze cannot be solved!")
    else:
        print("maze solved!")
    win.wait_for_close()

main()