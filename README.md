# Sudoku-Tkinter
An interactive Sudoku game built with Python and Tkinter, featuring a solver and hint system.

## Table of Contents

1. [Overview](#overview)
2. [Features](#features)
3. [Installation](#installation)
4. [Usage](#usage)
5. [Contributing](#contributing)
6. [License](#license)
7. [References](#references)

## Overview

This repository contains the source code for an interactive Sudoku game built using Python's Tkinter library. The application not only provides a graphical user interface for playing Sudoku but also comes with a real-time number validation and hint system. It utilizes backtracking algorithms for both solving and generating Sudoku puzzles.

![Sudoku Screenshot](https://github.com/black-fractal/Sudoku-Tkinter/blob/main/Sudoku-Tkinter.png)

## Features

- **Interactive Grid**: A 9x9 Sudoku grid where players can manually input numbers.
- **Number Validation**: Real-time checking to validate the numbers entered according to Sudoku rules.
- **Hint System**: Provides hints by filling in a correct number in the selected cell.
- **Solver Algorithm**: Integrated solver that uses backtracking to solve the puzzle.
- **Logging**: Detailed logging capabilities for debugging and development purposes.

## Installation

Follow these steps to get the game up and running:

### Prerequisites

- Python 3.x installed on your machine.

### Steps

1. Clone this repository to your local machine.
   ```
   git clone https://github.com/black-fractal/Sudoku-Tkinter.git
   ```
2. Navigate to the project directory.
   ```
   cd Sudoku-Tkinter
   ```
3. Run the game script.
   ```
   python sudoku.py
   ```

## Usage

1. Once the game starts, you'll see a 9x9 Sudoku grid with some cells already filled in.
2. Click on an empty cell to select it. The selected cell will be highlighted.
3. Press a number key (1-9) to fill that number into the selected cell.
   - If the number is correct according to Sudoku rules, it will be accepted.
   - If the number is incorrect, it will be marked in red.
4. Click the "Hint" button to get a hint. The hint will fill in the correct number in the selected cell.
5. Solve the Sudoku puzzle!

## Contributing

Contributions are welcome! If you have a feature request, bug report, or a suggestion, please feel free to open an issue or submit a pull request.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

## References

- Tkinter Documentation: [TkDocs](https://tkdocs.com/tutorial/index.html)
- Python Logging: [Python Official Documentation](https://docs.python.org/3/library/logging.html)

