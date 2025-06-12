# Sliding Tile Puzzle Game

This repository will contain a Python implementation of a 4x4 sliding tile puzzle. Users upload an image that is split into 16 equal tiles; the bottom-right tile will be empty. The game shuffles the tiles and allows users to slide pieces adjacent to the empty space. Once the original image is restored, a victory screen is shown, and the user can upload a new image to play again. The game window starts at a fixed size and tiles scale whenever the window is resized.

## Project Roadmap

1. **Setup (Completed)**: Initial project structure created with core game logic and a basic `tkinter` GUI.
2. **Image Handling (Completed)**: Implemented uploading an image and splitting it into tiles used in the GUI.
3. **Game Board Logic (Completed)**: Board is represented as a 2D array with shuffling and move validation.
4. **User Interaction (Completed)**: Basic GUI shows the tiles, supports mouse-controlled moves, and checks for a winning configuration after each move.
5. **Win State & Reset (Completed)**: When the puzzle is solved, a dialog offers to play again and upload a new image before the board is re-shuffled.
6. **Enhancements (In Progress)**: Basic move counter implemented in the GUI. Additional features like timers or a leaderboard are still to come.

## Development Notes

- Keep the code simple and organized. Start with a single module for the game logic, and another for the GUI.
- Avoid third-party dependencies where possible. Standard library modules like `tkinter`, `random`, and `PIL` (from Pillow) should suffice.
- Ensure image tiles are scaled to the same square size for consistent appearance.
- Add comments and docstrings to clarify functions and classes for future contributors.
- Include basic tests for the tile shuffle logic and winning-condition checks.

## How to Help

If you're contributing to this project:

1. Fork the repository and create a new branch for your feature or fix.
2. Write clear commit messages and keep pull requests focused on a single change.
3. Update documentation or add comments where your changes may need explanation.
4. Run linting or tests before submitting a PR when they become available.

## Future Ideas

- Support keyboard controls in addition to mouse input.
- Allow choosing different board sizes (e.g., 3x3 or 5x5) as a configuration option.
- Add sound effects or simple animations for tile movements.
- Package the game so it can be installed and run easily on different platforms.

