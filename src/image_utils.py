from typing import List, Optional
from PIL import Image

def split_image_to_tiles(
    path: str, size: int = 4, tile_size: Optional[int] = None
) -> List[List[Image.Image]]:
    """Load an image and split it into ``size`` x ``size`` tiles.

    Parameters
    ----------
    path:
        Path to the source image.
    size:
        Number of tiles along one dimension of the puzzle.
    tile_size:
        Optional fixed size for each square tile in pixels. If ``None`` (default)
        the tile size is derived from the input image dimensions.

    The returned list includes ``size`` lists of ``Image`` objects. The bottom-right
    tile corresponds to the empty slot and is included so indexes match tile
    numbers in :class:`src.game.SlidingPuzzle`.
    """
    img = Image.open(path)
    if tile_size is None:
        width, height = img.size
        tile_w = width // size
        tile_h = height // size
    else:
        tile_w = tile_h = tile_size
    img = img.resize((tile_w * size, tile_h * size))

    tiles: List[List[Image.Image]] = []
    for r in range(size):
        row = []
        for c in range(size):
            box = (c * tile_w, r * tile_h, (c + 1) * tile_w, (r + 1) * tile_h)
            row.append(img.crop(box))
        tiles.append(row)
    return tiles
