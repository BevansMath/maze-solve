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
    
    def _break_entrance_and_exit(self): # !! breakpoints not working here
        self._cells[0][0].has_top = False
        self._draw_cell(0,0)
        self._cells[self._num_cols - 1][self._num_rows - 1].has_bottom = False
        self._draw_cell(self._num_cols - 1, self._num_rows - 1)
        

    def _break_walls_all(self,i, j, seed=None):
        seed = random.seed()
        if seed is not None:
            random.seed(seed)

        self._cells[i][j].visited = True
        while True:
            next_index_list = []     

            potential_directions_idx= 0
            # determine which cells to visit
            # visiting the left
            if i > 0 and not self._cells[i-1][j].visited:
                next_index_list.append((i-1, j))
                potential_directions_idx +=1
            
            # right
            if i < self._num_cols - 1 and not self._cells[i + 1][j].visited:
                next_index_list.append((i+1, j))
                potential_directions_idx +=1
            
            # Move Up 
            if j > 0 and not self._cells[i][j - 1].visited:
                next_index_list.append((i, j - 1))
                potential_directions_idx += 1
            
            # Move Down
            if j < self._num_rows - 1 and not self._cells[i][j + 1].visited:
                next_index_list.append((i, j + 1))
                potential_directions_idx+= 1
            
            # Nowhere to move so we break from the statement
            if potential_directions_idx == 0:
                self._draw_cell(i,j)
            
                return
            #print(next_index_list) note that this returned [(1,0),(0,1)]
            #breakpoint()
            
            direction_idx= random.randrange(potential_directions_idx)
           
            next_index = next_index_list[direction_idx]
            
            # Next, delete the walls between this cell and the neighboring cells
            # Right wall
            if next_index[0] == i + 1:
                self._cells[i][j].has_adjacent_right = False
                self._cells[i + 1][j].has_adjacent_left = False
            # Left wall
            if next_index[0] == i - 1:
                self._cells[i][j].has_adjacent_left = False
                self._cells[i - 1][j].has_adjacent_right = False
            # Ceiling   
            if next_index[1] == j + 1:
                self._cells[i][j].has_bottom = False
                self._cells[i][j + 1].has_top = False
            # Floor
            if next_index[1] == j - 1:
                self._cells[i][j].has_top = False
                self._cells[i][j - 1].has_bottom = False

            # visit next cell recursively
            self._break_walls_all(next_index[0], next_index[1])


    def _reset_cells_visited(self):
        for col in self._cells:
            for cell in col:
                cell.visited=False
            
            # True if end cell, or if it leads to end cell
            # False if its a bad cell
    def _solve_r(self, i, j):
        self._animate()

        # visits the current cell
        self._cells[i][j].visited = True

        # if we have reached the end cell, done!
        if i == self._num_cols - 1 and j == self._num_rows - 1:
            return True

        # Otherwise, we move left if no wall exists and cell has not been visited
        if (i > 0 
            and not self._cells[i][j].has_adjacent_left 
            and not self._cells[i - 1][j].visited
        ):
            self._cells[i][j].draw_move(self._cells[i - 1][j])
            if self._solve_r(i - 1, j):
                return True
            else:
                self._cells[i][j].draw_move(self._cells[i - 1][j], True)

        # Otherwise, move right if there is no wall and cell has not been visited
        if (i < self._num_cols - 1 
            and not self._cells[i][j].has_adjacent_right
            and not self._cells[i + 1][j].visited
        ):
            self._cells[i][j].draw_move(self._cells[i+1][j])
            if self._solve_r(i+1,j):
                return True
            else:
                self._cells[i][j].draw_move(self._cells[i+1][j], True)

        # Otherwise, move up if there is no wall and cell has not been visited        
        if ( j > 0
        and not self._cells[i][j].has_top 
        and not self._cells[i][j-1].visited):
            self._cells[i][j].draw_move(self._cells[i][j - 1])
            if self._solve_r(i, j - 1):
                return True
            else:
                self._cells[i][j].draw_move(self._cells[i][j-1], True)

        # Otherwise, move down if there is no wall and cell has not been visited
        if (j < self._num_rows - 1
        and not self._cells[i][j].has_bottom 
        and not self._cells[i][j + 1].visited
        ):
            self._cells[i][j].draw_move(self._cells[i][j + 1])
            if self._solve_r(i, j + 1):
                return True
            else:
                self._cells[i][j].draw_move(self._cells[i][j + 1], True)
        
        return False

    def solve(self):
        return self._solve_r(0,0)