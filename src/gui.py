import tkinter as tk
from tkinter import filedialog, messagebox
from PIL import Image, ImageTk

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

    tiles = []
    photo_tiles = {}
    tile_w = tile_h = 0
    label_pad = 5

    def load_image(image_path: str) -> None:
        """Load ``image_path`` and create :mod:`PIL` image tiles."""
        nonlocal tiles
        tiles = split_image_to_tiles(image_path, puzzle.size)

    load_image(path)

    def resize_tiles(tile_size: int) -> None:
        nonlocal photo_tiles, tile_w, tile_h
        tile_w = tile_h = tile_size
        photo_tiles = {
            r * puzzle.size + c + 1: ImageTk.PhotoImage(
                tiles[r][c].resize((tile_size, tile_size), Image.NEAREST)
            )
            for r in range(puzzle.size)
            for c in range(puzzle.size)
        }

    resize_tiles(tiles[0][0].size[0])


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
                    root.update_idletasks()
                    resize_tiles(root.winfo_width() // puzzle.size)
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

    root.update_idletasks()
    label_height = move_label.winfo_height() + label_pad

    def on_resize(event: tk.Event) -> None:
        if event.widget is not root:
            return
        board_size = min(event.width, event.height - label_height)
        board_size = max(board_size, puzzle.size)
        board_size -= board_size % puzzle.size
        tile_size = board_size // puzzle.size
        new_w = board_size
        new_h = board_size + label_height
        if root.winfo_width() != new_w or root.winfo_height() != new_h:
            root.geometry(f"{new_w}x{new_h}")
        resize_tiles(tile_size)
        update_buttons()

    root.bind("<Configure>", on_resize)
    initial_size = tiles[0][0].size[0] * puzzle.size
    root.geometry(f"{initial_size}x{initial_size + label_height}")

    root.mainloop()


if __name__ == "__main__":
    main()
