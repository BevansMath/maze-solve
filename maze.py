from cell import Cell
import random
import time

class Maze:
    def __init__(
        self,
        x1,
        y1,
        num_rows,
        num_cols,
        cell_size_x,
        cell_size_y,
        win=None,
        seed=None,
    ):
        self._cells = []
        self._x1 = x1
        self._y1 = y1
        self._num_rows = num_rows
        self._num_cols = num_cols
        self._cell_size_x = cell_size_x
        self._cell_size_y = cell_size_y
        self._win = win
        if seed:
            random.seed(seed)

        self._creates_cells()
        self._break_entrance_and_exit()
        self._break_walls_all(0,0)
        self._reset_cells_visited()

    def _creates_cells(self):
        
        for i in range(self._num_cols):
            col_cells = []
            for j in range(self._num_rows):
                col_cells.append(Cell(self._win))
            self._cells.append(col_cells)
        for i in range(self._num_cols):
            for j in range(self._num_rows):
                self._draw_cell(i,j)                   

    def _draw_cell(self, i, j):
        if self._win is None:
            return
        x1 = self._x1 + i * self._cell_size_x
        y1 = self._y1 + j * self._cell_size_y
        x2 = x1 + self._cell_size_x
        y2 = y1 + self._cell_size_y
        self._cells[i][j].draw(x1,y1,x2,y2)
        self._animate()

    def _animate(self):
        if self._win is None:
            return
        self._win.redraw()
        time.sleep(0.05)
    
    def _break_entrance_and_exit(self):
        self._cells[0][0].has_top = False
        self._draw_cell(0,0)
        self._cells[self._num_cols - 1][self._num_rows - 1].has_bottom = False
        self._draw_cell(self._num_cols - 1, self._num_rows - 1)

    def _break_walls_all(self,i, j):
        
        self._cells[i][j].visited = True
        while True:
            next_index_list = []
            

            direction_idx = 0
            if i > 0 and not self._cells[i-1][j].visited:
                next_index_list.append((i-1, j))
                direction_idx +=1

            if i < self._num_cols - 1 and not self._cells[i + 1][j].visited:
                next_index_list.append((i+1, j))
                direction_idx +=1

            if j > 0 and not self._cells[i][j - 1].visited:
                next_index_list.append((i, j - 1))
                direction_idx += 1
            
            if j < self._num_rows - 1 and not self._cells[i][j + 1].visited:
                next_index_list.append((i, j + 1))
                direction_idx += 1

            if direction_idx == 0:
                self._draw_cell(i,j)
                return
            
            direction_idx2 = random.randrange(direction_idx)
            next_index = next_index_list[direction_idx2]

            if next_index[0] == i + 1:
                self._cells[i][j].has_adjacent_right = False
                self._cells[i + 1][j].has_adjacent_left = False

            if next_index[0] == i - 1:
                self._cells[i][j].has_adjacent_left = False
                self._cells[i - 1][j].has_adjacent_right = False
                
            if next_index[1] == j + 1:
                self._cells[i][j].has_bottom = False
                self._cells[i][j + 1].has_top = False

            if next_index[1] == j - 1:
                self._cells[i][j].has_top = False
                self._cells[i][j - 1].has_bottom = False

            self._break_walls_all(next_index[0], next_index[1])


    def _reset_cells_visited(self):
        for col in self._cells:
            for cell in col:
                cell.visited=False

    def _solve_r(self, i, j):
        self._animate()
        self._cells[i][j].visited = True

        if i == self._num_cols - 1 and j == self._num_rows - 1:
            return True

        if (i > 0 and not self._cells[i][j].has_adjacent_left and not self._cells[i - 1][j].visited):
            self._cells[i][j].draw_move(self._cells[i - 1][j])
            if self._solve_r(i - 1, j):
                return True
            else:
                self._cells[i][j].draw_move(self._cells[i - 1][j], True)

        if ( i < self._num_cols - 1 and not self._cells[i][j].has_adjacent_right and not self._cells[i + 1][j].visited):
            self._cells[i][j].draw_move(self._cells[i+1][j])
            if self._solve_r(i+1,j):
                return True
            else:
                self._cells[i][j].draw_move(self._cells[i+1][j], True)
                
        if ( j > 0 and not self._cells[i][j].has_top and not self._cells[i][j].draw_move(self._cells[i + 1][j], True)):
            self._cells[i][j].draw_move(self._cells[i][j - 1])
            if self._solve_r(i, j - 1):
                return True
            else:
                self._cells[i][j].draw_move(self._cells[i][j-1], True)

        if (j < self._num_rows - 1 and not self._cells[i][j].has_bottom and not self._cells[i][j + 1].visited):
            self._cells[i][j].draw_move(self._cells[i][j + 1])
            if self._solve_r(i, j + 1):
                return True
            else:
                self._cells[i][j].draw_move(self._cells[i][j + 1], True)
        
        return False

    def solve(self):
        return self._solve_r(0,0)
