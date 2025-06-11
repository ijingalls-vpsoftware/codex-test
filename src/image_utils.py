from typing import List
from PIL import Image

def split_image_to_tiles(path: str, size: int = 4) -> List[List[Image.Image]]:
    """Load an image and split it into ``size`` x ``size`` tiles.

    The returned list includes ``size`` lists of ``Image`` objects. The bottom-right
    tile corresponds to the empty slot and is included so indexes match tile
    numbers in :class:`src.game.SlidingPuzzle`.
    """
    img = Image.open(path)
    width, height = img.size
    tile_w = width // size
    tile_h = height // size
    img = img.resize((tile_w * size, tile_h * size))

    tiles: List[List[Image.Image]] = []
    for r in range(size):
        row = []
        for c in range(size):
            box = (c * tile_w, r * tile_h, (c + 1) * tile_w, (r + 1) * tile_h)
            row.append(img.crop(box))
        tiles.append(row)
    return tiles
