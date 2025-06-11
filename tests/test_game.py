import pytest

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
