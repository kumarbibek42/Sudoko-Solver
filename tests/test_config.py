import unittest
import config


class TestConfig(unittest.TestCase):

    def setUp(self) -> None:
        self.grid = [
            [3, 1, 6, 5, 7, 8, 4, 9, 2],
            [5, 2, 9, 1, 3, 4, 7, 6, 8],
            [4, 8, 7, 6, 2, 9, 5, 3, 1],
            [2, 6, 3, 4, 1, 5, 9, 8, 7],
            [9, 7, 4, 8, 6, 3, 1, 2, 5],
            [8, 5, 1, 7, 9, 2, 6, 4, 3],
            [1, 3, 8, 9, 4, 7, 2, 5, 6],
            [6, 9, 2, 3, 5, 1, 8, 7, 4],
            [7, 4, 5, 2, 8, 6, 3, 1, 9]
        ]
        config.ai_solved_grid = [
            [3, 0, 6, 0, 7, 8, 4, 9, 0],
            [5, 2, 9, 1, 3, 4, 7, 6, 8],
            [4, 8, 7, 6, 2, 9, 5, 3, 1],
            [2, 0, 3, 4, 1, 5, 9, 8, 7],
            [9, 7, 4, 8, 6, 0, 1, 2, 5],
            [8, 5, 1, 7, 0, 2, 6, 4, 3],
            [1, 3, 8, 9, 4, 7, 2, 5, 6],
            [6, 9, 2, 3, 5, 1, 8, 7, 4],
            [7, 4, 5, 2, 8, 6, 3, 1, 9]
        ]

    def update_ai_grid_entries(self):
        config.ai_solved_grid[0][3] = 2
        config.ai_solved_grid[3][1] = 3
        config.ai_solved_grid[4][5] = 4
        config.ai_solved_grid[5][4] = 4
        config.ai_solved_grid[0][8] = 4

    def test_is_first_box_correct(self):
        result = config.is_all_boxes_correct(self.grid)
        self.assertTrue(result)
        self.grid[0][0] = 1
        result = config.is_all_boxes_correct(self.grid)
        self.assertFalse(result)

    def test_is_middle_box_correct(self):
        result = config.is_all_boxes_correct(self.grid)
        self.assertTrue(True)
        self.grid[3][3] = 1
        result = config.is_all_boxes_correct(self.grid)
        self.assertFalse(result)

    def test_is_last_box_correct(self):
        result = config.is_all_boxes_correct(self.grid)
        self.assertTrue(True)
        self.grid[6][6] = 1
        result = config.is_all_boxes_correct(self.grid)
        self.assertFalse(result)

    def test_is_row_assignment_correct(self):
        row_ind = 0
        num = 1
        result = config.is_row_assignment_correct(row_ind, num)
        self.assertTrue(result)
        num = 3
        result = config.is_row_assignment_correct(row_ind, num)
        self.assertFalse(result)

    def test_is_column_assignment_correct(self):
        column_ind = 1
        num = 6
        result = config.is_column_assignment_correct(column_ind, num)
        self.assertTrue(result)
        num = 2
        result = config.is_column_assignment_correct(column_ind, num)
        self.assertFalse(result)

    def test_is_box_assignment_correct(self):
        row_ind = 1
        column_ind = 1
        num = 1
        result = config.is_box_assignment_correct(row_ind, column_ind, num)
        self.assertTrue(result)
        num = 2
        result = config.is_box_assignment_correct(row_ind, column_ind, num)
        self.assertFalse(result)
        row_ind = 5
        column_ind = 5
        num = 9
        result = config.is_box_assignment_correct(row_ind, column_ind, num)
        self.assertTrue(result)
        num = 3
        result = config.is_box_assignment_correct(row_ind, column_ind, num)
        self.assertTrue(result)
        num = 2
        result = config.is_box_assignment_correct(row_ind, column_ind, num)
        self.assertFalse(result)

    def test_is_any_cell_empty(self):
        empty_cell = [0, 0]
        result = config.is_any_cell_empty(empty_cell)
        config.ai_solved_grid[empty_cell[0]][empty_cell[1]] = 1
        self.assertTrue(result)
        self.assertEqual(empty_cell, [0, 1])
        result = config.is_any_cell_empty(empty_cell)
        self.assertTrue(result)
        self.assertEqual(empty_cell, [0, 3])
        self.update_ai_grid_entries()
        result = config.is_any_cell_empty(empty_cell)
        self.assertFalse(result)

if __name__ == '__main__':
    unittest.main()