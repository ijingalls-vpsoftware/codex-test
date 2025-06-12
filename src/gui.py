import tkinter as tk
from tkinter import filedialog, messagebox
from PIL import ImageTk

from .game import SlidingPuzzle
from .image_utils import split_image_to_tiles

BOARD_SIZE = 500  # initial width/height of the puzzle board in pixels


def main() -> None:
    puzzle = SlidingPuzzle()
    puzzle.shuffle()

    root = tk.Tk()
    root.title("Sliding Tile Puzzle")
    root.geometry(f"{BOARD_SIZE}x{BOARD_SIZE + 40}")
    root.minsize(300, 300)
    root.rowconfigure(0, weight=1)
    root.columnconfigure(0, weight=1)

    board_frame = tk.Frame(root, width=BOARD_SIZE, height=BOARD_SIZE)
    board_frame.grid(row=0, column=0, sticky="nsew")
    board_frame.grid_propagate(False)
    for i in range(puzzle.size):
        board_frame.rowconfigure(i, weight=1)
        board_frame.columnconfigure(i, weight=1)


    # Ask user to select an image to use for the puzzle tiles
    path = filedialog.askopenfilename(
        title="Select an image",
        filetypes=[("Image files", "*.png *.jpg *.jpeg *.gif")],
    )
    if not path:
        return

    tiles = []  # PIL images for each tile
    photo_tiles = {}  # Tk images scaled to current tile size
    tile_w = tile_h = BOARD_SIZE // puzzle.size

    def _create_photo_tiles(width: int, height: int) -> None:
        nonlocal photo_tiles, tile_w, tile_h
        tile_w, tile_h = width, height
        photo_tiles = {
            r * puzzle.size + c + 1: ImageTk.PhotoImage(
                tiles[r][c].resize((width, height))
            )
            for r in range(puzzle.size)
            for c in range(puzzle.size)
        }

    def load_image(image_path: str) -> None:
        """Load ``image_path`` and create :mod:`PIL` image tiles."""
        nonlocal tiles
        tiles = split_image_to_tiles(image_path, puzzle.size)
        _create_photo_tiles(tile_w, tile_w)

    load_image(path)

    buttons = []
    move_label = tk.Label(root, text=f"Moves: {puzzle.moves}")
    move_label.grid(row=1, column=0, pady=(5, 0))

    def update_buttons():
        for r in range(puzzle.size):
            for c in range(puzzle.size):
                value = puzzle.board[r][c]
                btn = buttons[r][c]
                if value == 0:
                    btn.config(image="", text="", width=tile_w, height=tile_h)
                else:
                    btn.config(
                        image=photo_tiles[value], text="", width=tile_w, height=tile_h
                    )
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
                    _create_photo_tiles(
                        board_frame.winfo_width() // puzzle.size,
                        board_frame.winfo_height() // puzzle.size,
                    )
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
                board_frame,
                image=img,
                text=txt,
                width=tile_w,
                height=tile_h,
                command=lambda r=r, c=c: on_click(r, c),
            )
            btn.grid(row=r, column=c, padx=1, pady=1, sticky="nsew")
            row.append(btn)
        buttons.append(row)

    def on_resize(event) -> None:
        _create_photo_tiles(event.width // puzzle.size, event.height // puzzle.size)
        update_buttons()

    board_frame.bind("<Configure>", on_resize)

    root.mainloop()


if __name__ == "__main__":
    main()
