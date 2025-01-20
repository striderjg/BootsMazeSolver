import unittest

from maze import Maze

class Test(unittest.TestCase):
    def test_maze_create(self):
        num_cols = 12
        num_rows = 10
        
        m1 = Maze(0, 0, num_rows, num_cols, 20, 20)
        self.assertEqual(
            len(m1._cells), 
            num_cols
        )
        self.assertEqual(
            len(m1._cells[0]),
            num_rows
        )
    def test_maze_reset_visited(self):
        num_cols = num_rows = 10
        m1 = Maze(0, 0, num_rows, num_cols, 20, 20)
        m1._break_entrance_and_exit()
        m1.break_walls()
        m1._reset_cells_visited()
        for i in range(num_cols):
            for j in range(num_rows):
                assert m1._cells[i][j].visited == False
        
if __name__ == "__main__":
    unittest.main()