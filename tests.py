import unittest

from maze import Maze

class Test:
    def test_maze_creates_cells(self): #Creates_cells() method creates the correct number of cells
        num_cols = 12
        num_rows = 10
        m1 = Maze(0,0, num_rows, num_cols, 10, 10)
        self.assertEqual(
            len(m1._cells),
           num_cols,
        )
        self.assertEqual(
            len(m1._cells[0]),
            num_rows,
        )
    def test_maze_remove_walls(self):
        num_cols = 12
        num_rows = 10
        m2 = Maze(0,0, num_rows, num_cols, 10, 10)
        self.assertEqual(
            m2._cells[0][0].has_top,
            False,
           )
        self.assertEqual(
            m2._cells[num_rows - 1][num_cols - 1].has_bottom,
            False,
        )
    

    def test_maze_reset_cells_visited(self):
        num_cols = 12
        num_rows = 10
        m1 = Maze(0,0, num_rows, num_cols, 10, 10)
        for col in m1._cells:
            for cell in col:
                self.assertEqual(
                    cell.visited,
                    False, 
                    
                )
if __name__ == "__main__": # Driver function to test main script
    unittest.main()