# Conway's Game of Life

An interactive implementation of Conway's Game of Life,
built with Python and Pygame.

The project simulates a cellular automaton based on Conway's
rules. Users can create their own patterns, control the
simulation speed, and observe how the board evolves.

## Features

- Interactive 40x40 cell grid
- Add and remove living cells using the mouse
- Start and pause the simulation
- Generate random cell configurations
- Clear the board
- Adjust simulation speed using arrow keys
- Display the current generation and simulation speed
- Automated tests for stable and oscillating patterns

## Technologies

- Python
- Pygame 2.6.1
- pytest 8.3.4

## Project Structure

```text
GameOfLife/
├── main.py
├── game_logic.py
├── test_game_logic.py
├── requirements.txt
├── README.md
└── .gitignore
```

- `main.py` - Pygame interface, rendering, and event handling
- `game_logic.py` - cellular automaton simulation logic
- `test_game_logic.py` - automated tests for the simulation
- `requirements.txt` - project dependencies

## Controls

| Control | Action |
|---------|--------|
| Mouse click | Add or remove a cell |
| Space | Start / pause simulation |
| C | Clear the board and pause |
| G | Generate a random configuration |
| Up arrow | Increase simulation speed |
| Down arrow | Decrease simulation speed |

## How It Works

Each cell on the board can be either alive or dead.

The simulation follows Conway's Game of Life rules:

1. A living cell with fewer than two living neighbors dies.
2. A living cell with two or three living neighbors survives.
3. A living cell with more than three living neighbors dies.
4. A dead cell with exactly three living neighbors becomes alive.

Living cells are represented using a Python set containing
coordinate tuples.

For each generation, the algorithm examines living cells
and their neighbors to determine the next state of the board.

The simulation logic is separated from the graphical
interface, allowing it to be tested independently of Pygame.

Cells outside the board boundaries are not considered.

## Installation

The project was tested using Python 3.13.

### 1. Clone the repository

```bash
git clone https://github.com/Blqcky23/GameOfLife.git
cd GameOfLife
```

### 2. Create a virtual environment

```bash
python -m venv .venv
```

### 3. Activate the environment

**Windows PowerShell:**

```powershell
.\.venv\Scripts\Activate.ps1
```

**Linux / macOS:**

```bash
source .venv/bin/activate
```

### 4. Install dependencies

```bash
python -m pip install -r requirements.txt
```

### 5. Run the game

```bash
python main.py
```

## Running Tests

Run the automated tests with:

```bash
python -m pytest -v
```

The tests cover two classic Game of Life patterns:

- **Block** - a stable pattern that remains unchanged.
- **Blinker** - a period-2 oscillator that alternates
  between vertical and horizontal configurations.

The tests run without launching the Pygame interface.

## Limitations

- The board has fixed dimensions (40x40).
- Cells outside the board are not simulated.
- Simulation speed is frame-based and therefore approximate.
- There is no save/load functionality for cell configurations.

## Project Status

Completed educational project demonstrating Python
programming, algorithm implementation, separation of
application logic, event handling, and automated testing.
