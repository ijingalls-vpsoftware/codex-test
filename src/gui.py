import tkinter as tk
from tkinter import filedialog, messagebox
from PIL import ImageTk

from .game import SlidingPuzzle
from .image_utils import split_image_to_tiles


def main() -> None:
    puzzle = SlidingPuzzle()
    puzzle.shuffle()

    root = tk.Tk()
    root.title("Sliding Tile Puzzle")

    # Ask user to select an image to use for the puzzle tiles
    path = filedialog.askopenfilename(
        title="Select an image",
        filetypes=[("Image files", "*.png *.jpg *.jpeg *.gif")],
    )
    if not path:
        return

    # Load and split the selected image
    tiles = split_image_to_tiles(path, puzzle.size)
    photo_tiles = {
        r * puzzle.size + c + 1: ImageTk.PhotoImage(tiles[r][c])
        for r in range(puzzle.size)
        for c in range(puzzle.size)
    }

    buttons = []
    tile_w, tile_h = tiles[0][0].size

    def update_buttons():
        for r in range(puzzle.size):
            for c in range(puzzle.size):
                value = puzzle.board[r][c]
                btn = buttons[r][c]
                if value == 0:
                    btn.config(image="", text="")
                else:
                    btn.config(image=photo_tiles[value], text="")

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
            if value == 0:
                img = ""
                txt = ""
            else:
                img = photo_tiles[value]
                txt = ""
            btn = tk.Button(
                root,
                image=img,
                text=txt,
                width=tile_w,
                height=tile_h,
                command=lambda r=r, c=c: on_click(r, c),
            )
            btn.grid(row=r, column=c, padx=1, pady=1)
            row.append(btn)
        buttons.append(row)

    root.mainloop()


if __name__ == "__main__":
    main()
