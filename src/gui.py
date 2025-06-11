import tkinter as tk
from tkinter import messagebox

from .game import SlidingPuzzle


def main() -> None:
    puzzle = SlidingPuzzle()
    puzzle.shuffle()

    root = tk.Tk()
    root.title("Sliding Tile Puzzle")

    buttons = []

    def update_buttons():
        for r in range(puzzle.size):
            for c in range(puzzle.size):
                value = puzzle.board[r][c]
                btn = buttons[r][c]
                btn.config(text=str(value) if value else "")

    def on_click(r: int, c: int):
        if puzzle.move(r, c):
            update_buttons()
            if puzzle.is_solved():
                messagebox.showinfo("Congrats!", "You solved the puzzle!")
                puzzle.shuffle()
                update_buttons()

    for r in range(puzzle.size):
        row = []
        for c in range(puzzle.size):
            value = puzzle.board[r][c]
            text = str(value) if value else ""
            btn = tk.Button(root, text=text, width=4, height=2,
                            command=lambda r=r, c=c: on_click(r, c))
            btn.grid(row=r, column=c, padx=2, pady=2)
            row.append(btn)
        buttons.append(row)

    root.mainloop()


if __name__ == "__main__":
    main()
