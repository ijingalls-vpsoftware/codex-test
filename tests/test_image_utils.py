import os
import sys
from pathlib import Path
from PIL import Image

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from src.image_utils import split_image_to_tiles

def test_split_image_to_tiles(tmp_path: Path) -> None:
    # Create a simple test image
    img = Image.new("RGB", (80, 80), "blue")
    path = tmp_path / "test.png"
    img.save(path)

    tiles = split_image_to_tiles(str(path))
    assert len(tiles) == 4
    for row in tiles:
        assert len(row) == 4
        for tile in row:
            assert tile.size == (20, 20)
