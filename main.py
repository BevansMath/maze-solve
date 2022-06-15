from windows import Window
from maze import Maze
import sys


def main():         # Create the window screen 
    screen_x = 800
    screen_y = 600
    win = Window(screen_x, screen_y)

    num_rows = 24 # Define the number of rows and columns to create the grid
    num_cols = 32
    margin = 50

                   # Define cell size as screen size coordinates * margins divided by the rows and colums
    cell_size_x = (screen_x - 2 * margin)/ num_cols
    cell_size_y = (screen_y - 2 * margin) / num_rows
  

    sys.setrecursionlimit(100000)

    maze = Maze(margin, margin, num_rows, num_cols, cell_size_x, cell_size_y, win)
    
    print("maze created")
    is_solveable = maze.solve()
    if not is_solveable:
        print("Maze cannot be solved!")
    else:
        print("maze solved!")
    win.wait_for_close()

main()