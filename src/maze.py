import time
import random
from cell import Cell

class Maze():
    def __init__(self, x1, y1, num_rows, num_cols, cell_size_x, cell_size_y, win = None, seed=None):

        self._x1 = x1
        self._y1 = y1
        self._num_rows = num_rows
        self._num_cols = num_cols
        self._cell_size_x = cell_size_x
        self._cell_size_y = cell_size_y
        self._win = win
        self._end = (num_cols - 1, num_rows - 1)
        self._create_cells()
        if seed is not None:
            random.seed(seed)
    
    def _create_cells(self):
        self._cells = []
        for i in range(self._num_cols):
            rows = []
            for j in range(self._num_rows):
                cell = Cell(self._win)
                rows.append(cell)
            self._cells.append(rows)

        if self._win is not None:
            for i in range(self._num_cols):
                for j in range(self._num_rows):
                    self._draw_cell(i, j)
            
            self._break_entrance_and_exit()
            self._break_walls_r(0, 0)
            self._reset_cells_visited()

    def _break_entrance_and_exit(self):
        self._break_walls(0, 0, ["top",])
        self._draw_cell(0, 0)
        self._break_walls(self._end[0], self._end[1], ["bottom",])
        self._draw_cell(self._end[0], self._end[1])

    def _break_walls(self, i, j, walls):
        for wall in walls:
            match wall:
                case "left":
                    self._cells[i][j].has_left_wall = False
                    self._draw_cell(i, j)
                    
                case "right":
                    self._cells[i][j].has_right_wall = False
                    self._draw_cell(i, j)
                    
                case "top":
                    self._cells[i][j].has_top_wall = False
                    self._draw_cell(i, j)
                    
                case "bottom":
                    self._cells[i][j].has_bottom_wall = False
                    self._draw_cell(i, j)
                case _:
                    raise ValueError("Invalid wall direction")
    
    def _break_walls_r(self, i, j):
        self._cells[i][j].visited = True
        while True:
            
            possible_moves = []
            if i > 0:
                if self._cells[i - 1][j].visited == False:
                    possible_moves.append((-1, 0, "left"))
            if i < self._num_cols - 1:
                if self._cells[i + 1][j].visited == False:
                    possible_moves.append((1, 0, "right"))
            if j > 0:
                if self._cells[i][j - 1].visited == False:
                    possible_moves.append((0, -1, "top"))
            if j < self._num_rows - 1:
                if self._cells[i][j + 1].visited == False:
                    possible_moves.append((0, 1, "bottom"))
            if len(possible_moves) == 0:
                self._draw_cell(i, j)
                return
            move = random.randint(0, len(possible_moves) - 1)
            
            self._break_walls(i, j, [possible_moves[move][2]])

            match possible_moves[move][2]:
                case "left":
                    self._break_walls(i - 1, j, ["right"])
                case "right":
                    self._break_walls(i + 1, j, ["left"])
                case "top":
                    self._break_walls(i, j - 1, ["bottom"])
                case "bottom":
                    self._break_walls(i, j + 1, ["top"])
                case _:
                    raise ValueError("Invalid direction in wall loop")
            self._break_walls_r(i + possible_moves[move][0], j + possible_moves[move][1])
            
    def _reset_cells_visited(self):
        for i in range(self._num_cols):
            for j in range(self._num_rows):
                self._cells[i][j].visited = False

    def _draw_cell(self, i, j):
        x1 = self._x1 + (i * self._cell_size_x)
        y1 = self._y1 + (j * self._cell_size_y)
        x2 = x1 + self._cell_size_x
        y2 = y1 + self._cell_size_y
        self._cells[i][j].draw(x1, y1, x2, y2)
        self._animate()
    
    def _animate(self):
        self._win.redraw()
        time.sleep(0.05)
    
    def _solve_r(self, i, j):
        self._animate()
        self._cells[i][j].visited = True
        if i == self._end[0] and j == self._end[1]:
            return True
        possible_moves = []
        if i > 0:
            if self._cells[i - 1][j].visited == False and not self._cells[i][j].has_left_wall and not self._cells[i - 1][j].has_right_wall:
                possible_moves.append((-1, 0))
        if i < self._num_cols - 1:
            if self._cells[i + 1][j].visited == False and not self._cells[i][j].has_right_wall and not self._cells[i + 1][j].has_left_wall:
                possible_moves.append((1, 0))
        if j > 0:
            if self._cells[i][j - 1].visited == False and not self._cells[i][j].has_top_wall and not self._cells[i][j - 1].has_bottom_wall:
                possible_moves.append((0, -1))
        if j < self._num_rows - 1:
            if self._cells[i][j + 1].visited == False and not self._cells[i][j].has_bottom_wall and not self._cells[i][j + 1].has_top_wall:
                possible_moves.append((0, 1))
            
        for move in possible_moves:
            self._cells[i][j].draw_move(self._cells[i + move[0]][j + move[1]])
            if self._solve_r(i + move[0], j + move[1]):
                return True
            else:
                self._cells[i][j].draw_move(self._cells[i + move[0]][j + move[1]], True)
        return False



    def are_all_cells_unvisited(self):
        for i in range(self._num_cols):
            for j in range(self._num_rows):
                if self._cells[i][j].visited == True:
                    return False
        return True

    def solve(self):
        return self._solve_r(0, 0)