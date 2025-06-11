import random
from typing import List, Tuple

class SlidingPuzzle:
    """Core game logic for a sliding tile puzzle.

    Attributes
    ----------
    size: int
        The dimension of the puzzle grid.
    board: List[List[int]]
        Current puzzle state where ``0`` represents the empty slot.
    moves: int
        Counter tracking how many valid moves have been made since the
        last shuffle or reset.
    """

    def __init__(self, size: int = 4):
        self.size = size
        self.reset()

    def reset(self) -> None:
        """Reset the board to the solved configuration."""
        self.board = [
            [r * self.size + c + 1 for c in range(self.size)]
            for r in range(self.size)
        ]
        self.board[-1][-1] = 0  # empty slot
        self.moves = 0

    def shuffle(self) -> None:
        """Shuffle the board tiles into a solvable configuration."""
        tiles = list(range(1, self.size * self.size))
        while True:
            random.shuffle(tiles)
            tiles.append(0)
            if self._is_solvable(tiles):
                break
            tiles.pop()
        self.board = [
            tiles[i * self.size : (i + 1) * self.size]
            for i in range(self.size)
        ]
        self.moves = 0

    def _is_solvable(self, tiles: List[int]) -> bool:
        inv_count = 0
        for i in range(len(tiles) - 1):
            for j in range(i + 1, len(tiles)):
                if tiles[i] and tiles[j] and tiles[i] > tiles[j]:
                    inv_count += 1
        if self.size % 2 == 1:
            return inv_count % 2 == 0
        blank_row = self.size - (tiles.index(0) // self.size)
        if blank_row % 2 == 0:
            return inv_count % 2 == 1
        return inv_count % 2 == 0

    def move(self, row: int, col: int) -> bool:
        """Move a tile at (row, col) if it is adjacent to the empty slot."""
        erow, ecol = self._find_empty()
        if abs(erow - row) + abs(ecol - col) != 1:
            return False
        self.board[erow][ecol], self.board[row][col] = (
            self.board[row][col],
            self.board[erow][ecol],
        )
        self.moves += 1
        return True

    def _find_empty(self) -> Tuple[int, int]:
        for r in range(self.size):
            for c in range(self.size):
                if self.board[r][c] == 0:
                    return r, c
        raise ValueError("No empty tile found")

    def is_solved(self) -> bool:
        """Check if the board is in a winning configuration."""
        expected = list(range(1, self.size * self.size)) + [0]
        tiles = [self.board[r][c] for r in range(self.size) for c in range(self.size)]
        return tiles == expected
