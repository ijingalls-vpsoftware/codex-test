import os
import sys
import pytest

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from src.game import SlidingPuzzle


def test_shuffle_solvable():
    puzzle = SlidingPuzzle()
    puzzle.shuffle()
    assert not puzzle.is_solved()
    # ensure puzzle contains correct tiles
    tiles = sorted(
        t for row in puzzle.board for t in row
    )
    assert tiles == list(range(16))


def test_move_and_solve():
    puzzle = SlidingPuzzle()
    assert puzzle.is_solved()
    # move the tile left of the empty spot
    puzzle.move(puzzle.size - 1, puzzle.size - 2)
    assert not puzzle.is_solved()
    puzzle.move(puzzle.size - 1, puzzle.size - 1)
    assert puzzle.is_solved()


def test_move_counter_resets_on_shuffle():
    puzzle = SlidingPuzzle()
    puzzle.shuffle()
    assert puzzle.moves == 0
    erow, ecol = puzzle._find_empty()
    if erow > 0:
        puzzle.move(erow - 1, ecol)
    else:
        puzzle.move(erow + 1, ecol)
    assert puzzle.moves == 1
    puzzle.shuffle()
    assert puzzle.moves == 0
