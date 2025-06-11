# Sliding Tile Puzzle Game

This repository will contain a Python implementation of a 4x4 sliding tile puzzle. Users will upload an image that is split into 16 equal tiles; the bottom-right tile will be empty. The game shuffles the tiles and allows users to slide pieces adjacent to the empty space. Once the original image is restored, a victory screen is shown, and the user can upload a new image to play again.

## Project Roadmap

1. **Setup (Completed)**: Initial project structure created with core game logic and a basic `tkinter` GUI.
2. **Image Handling**: Implement image upload support and a function to split the image into 4x4 tiles (15 tiles plus one empty slot).
3. **Game Board Logic**: Represent the board as a 2D array and implement mechanics to shuffle tiles and determine valid moves (left, right, up, down from the empty space).
4. **User Interaction**: Create a basic GUI that displays the tiles, allows tile movement via mouse clicks, and checks for a winning configuration after each move.
5. **Win State & Reset**: Display a win screen or message when the player solves the puzzle, then provide an option to upload a new image and start over.
6. **Enhancements**: Consider optional features such as move counters, timers, or a leaderboard.

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

