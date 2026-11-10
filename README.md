
# Conway's Game of Life

An interactive implementation of Conway's Game of Life
built with Python and Pygame.

The application simulates cellular automata using the
classic rules of Conway's Game of Life.

## Features

- Interactive 40x40 cell grid
- Add and remove living cells with mouse clicks
- Start and pause the simulation
- Generate random cell configurations
- Clear the board
- Adjust simulation speed
- Display the generation counter and simulation speed
- Automated tests for cellular automata patterns

## Technologies

- Python
- Pygame
- pytest

## Project Structure

- `main.py` - Pygame interface and event handling
- `game_logic.py` - simulation logic
- `test_game_logic.py` - automated tests
- `requirements.txt` - project dependencies

## Controls

| Key | Action |
|-----|--------|
| Left mouse button | Add/remove a cell |
| Space | Start/pause |
| C | Clear the board |
| G | Generate random cells |
| Up arrow | Increase simulation speed |
| Down arrow | Decrease simulation speed |

## How It Works

Each cell is either alive or dead.

The next generation is calculated using four rules:

1. A living cell with fewer than two living neighbors dies.
2. A living cell with two or three living neighbors survives.
3. A living cell with more than three living neighbors dies.
4. A dead cell with exactly three living neighbors becomes alive.

The simulation uses a set of coordinates to represent
living cells and considers only neighbors within the
board boundaries.

The simulation logic is separated from the Pygame interface.

## Installation

Create a virtual environment:

    python -m venv .venv

Install dependencies:

    python -m pip install -r requirements.txt

Run the application:

    python main.py

## Tests

Run:

    python -m pytest -v

The tests verify:

- Block (stable pattern)
- Blinker (period-2 oscillator)

## Limitations

- The board has fixed dimensions.
- Cells outside the board are not considered.
- Simulation speed is based on the frame rate and is approximate.
