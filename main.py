from windows import Window
from cell import Cell
from maze import Maze


def main():
    win = Window(screen_x, screen_y)

    num_rows = 12
    num_cols = 16
    margin = 50
    screen_x = 800
    screen_y = 600

    cell_size_x = (screen_x - 2 * margin)/ num_cols
    cell_size_y = (screen_y - 2 * margin) / num_rows
    maze = Maze(margin, margin, num_rows, num_cols, cell_size_x, cell_size_y, win)

    c = Cell(win)
    c.has_adjacent_left = False
    c.draw(50,50,100,100)

    c = Cell(win)
    c.has_adjacent_right = False
    c.draw(125,125,200,200)

    c = Cell(win)
    c.has_bottom = False
    c.draw(225,225,250,250)

    c = Cell(win)
    c.has_top = False
    c.draw(300,300,500,500)
    
    #l = Line(Point(50,50), Point(400,400))
    #win.draw_line(l,"black")
    #win.wait_for_close()

    sys.setrecursionlimit(10000)

    maze = Maze()
    print("maze created")
    is_solveable = maze.solve()
    if not is_solveable:
        print("Maze cannot be solved!")
    else:
        print("maze solved!")
    # win.wait_for_close()

main()