from enum import Enum
from typing import List, NamedTuple, Callable, Optional
import random
from math import sqrt
from generic_search import dfs, bfs, node_to_path, astar, Node


class Cell(str, Enum):
    EMPTY = " "
    BLOCKED = "X"
    START = "S"
    GOAL = "G"
    PATH = "*"

class MazeLocation(NamedTuple):
    row: int
    column: int

class Maze:
    def __init__(self, rows=10, columns=10, sparseness=0.2, start= MazeLocation(0, 0), goal=MazeLocation(9,9)) -> None:
        # initializing maze
        self._rows=rows
        self._columns=columns
        self.sparseness=sparseness
        self.start = start
        self.goal = goal
        self._grid = [[Cell.EMPTY for c in range(columns)] for r in range(rows)]


        for r in range(rows):
            # populate grid with blocked values
            self._randomly_fill(rows, columns, sparseness)
            # fill the start and goal values in maze
            self._grid[start.row][start.column] = Cell.START
            self._grid[goal.row][goal.column] = Cell.GOAL

    def _randomly_fill(self, rows : int, columns : int , sparseness : float):
        for r in range(rows):
            for c in range(columns):
                if random.uniform(0, 1.0) < sparseness:
                    self._grid[r][c] = Cell.BLOCKED

    def __str__(self):
        output = ""
        for row in self._grid:
            output += "".join([c.value for c in row])+ "\n"

        return output


maze = Maze()
print(maze)


