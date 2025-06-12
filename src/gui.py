import tkinter as tk
from tkinter import filedialog, messagebox
from PIL import ImageTk

TILE_SIZE = 100

from .game import SlidingPuzzle
from .image_utils import split_image_to_tiles


def main() -> None:
    puzzle = SlidingPuzzle()
    puzzle.shuffle()

    root = tk.Tk()
    root.title("Sliding Tile Puzzle")
    window_size = puzzle.size * TILE_SIZE
    root.geometry(f"{window_size}x{window_size + 40}")
    root.resizable(False, False)

    # Ask user to select an image to use for the puzzle tiles
    path = filedialog.askopenfilename(
        title="Select an image",
        filetypes=[("Image files", "*.png *.jpg *.jpeg *.gif")],
    )
    if not path:
        return

    tiles = []
    photo_tiles = {}
    tile_w = tile_h = TILE_SIZE

    def load_image(image_path: str) -> None:
        """Load ``image_path`` and create :mod:`PIL` image tiles."""
        nonlocal tiles, photo_tiles, tile_w, tile_h
        tiles = split_image_to_tiles(image_path, puzzle.size, TILE_SIZE)
        photo_tiles = {
            r * puzzle.size + c + 1: ImageTk.PhotoImage(tiles[r][c])
            for r in range(puzzle.size)
            for c in range(puzzle.size)
        }
        tile_w, tile_h = tiles[0][0].size

    load_image(path)

    buttons = []
    move_label = tk.Label(root, text=f"Moves: {puzzle.moves}")
    move_label.grid(row=puzzle.size, column=0, columnspan=puzzle.size, pady=(5, 0))

    def update_buttons():
        for r in range(puzzle.size):
            for c in range(puzzle.size):
                value = puzzle.board[r][c]
                btn = buttons[r][c]
                if value == 0:
                    btn.config(image="", text="")
                else:
                    btn.config(image=photo_tiles[value], text="")
        move_label.config(text=f"Moves: {puzzle.moves}")

    def on_click(r: int, c: int):
        if puzzle.move(r, c):
            update_buttons()
            if puzzle.is_solved():
                again = messagebox.askyesno(
                    "Congrats!", "You solved the puzzle! Play again?"
                )
                if not again:
                    root.quit()
                    return
                new_path = filedialog.askopenfilename(
                    title="Select an image",
                    filetypes=[("Image files", "*.png *.jpg *.jpeg *.gif")],
                )
                if new_path:
                    load_image(new_path)
                    for r in range(puzzle.size):
                        for c in range(puzzle.size):
                            btn = buttons[r][c]
                            btn.config(width=tile_w, height=tile_h)
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
