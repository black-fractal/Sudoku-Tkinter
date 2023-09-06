import tkinter as tk
import logging
import random
from datetime import datetime

# Initialize Logging
logging.basicConfig(
    level=logging.DEBUG,
    format='%(asctime)s - %(levelname)s - %(message)s',
    handlers=[
        logging.FileHandler("sudoku.log", mode='a'),
        logging.StreamHandler()
    ]
)

class Sudoku:
    def __init__(self, root):
        logging.debug("Initializing Sudoku game.")
        self.root = root
        self.root.title('Sudoku')
        self.canvas = tk.Canvas(self.root, width=550, height=550)
        self.canvas.pack()
        self.board = self.generate_board()
        self.solved_board = [row.copy() for row in self.board]
        self.solve_board(self.solved_board)
        self.selected_cell = None
        self.fixed_cells = set()
        self.unique_counter = 0  # Moved inside class
        self.setup_board()
        self.setup_controls()

    def setup_board(self):
        for i in range(9):
            for j in range(9):
                if self.board[i][j] != 0:
                    self.fixed_cells.add((i, j))
        self.fill_grid()
        self.canvas.bind("<Button-1>", self.select_cell)

    def setup_controls(self):
        tk.Button(self.root, text='Hint', command=self.hint).pack()

    def is_valid_move(self, board, row, col, num):
        if num in board[row]:
            return False
        if num in [board[i][col] for i in range(9)]:
            return False
        row_start, col_start = 3 * (row // 3), 3 * (col // 3)
        for i in range(row_start, row_start + 3):
            for j in range(col_start, col_start + 3):
                if board[i][j] == num:
                    return False
        return True

    def solve_board(self, board):
        for row in range(9):
            for col in range(9):
                if board[row][col] == 0:
                    for num in range(1, 10):
                        if self.is_valid_move(board, row, col, num):
                            board[row][col] = num
                            if self.solve_board(board):
                                return True
                            board[row][col] = 0
                    return False
        return True

    def generate_board(self):
        solved_board = self.generate_solved_board()
        return self.generate_puzzle(solved_board)

    def generate_solved_board(self):
        board = [[0 for _ in range(9)] for _ in range(9)]
        for _ in range(17):
            row, col, num = random.randint(0, 8), random.randint(0, 8), random.randint(1, 9)
            while not self.is_valid_move(board, row, col, num) or board[row][col] != 0:
                row, col, num = random.randint(0, 8), random.randint(0, 8), random.randint(1, 9)
            board[row][col] = num
        self.solve_board(board)
        return board

    def generate_puzzle(self, board, num_removed=20):
        puzzle = [row[:] for row in board]
        for _ in range(num_removed):
            row, col = random.randint(0, 8), random.randint(0, 8)
            while puzzle[row][col] == 0:
                row, col = random.randint(0, 8), random.randint(0, 8)
            puzzle[row][col] = 0
        return puzzle

    def fill_grid(self):
        logging.debug("Filling grid.")
        self.canvas.delete("numbers")
        self.canvas.delete("grid")
        for i in range(9):
            for j in range(9):
                if self.board[i][j] != 0:
                    x, y = 40 + j * 60, 40 + i * 60
                    self.canvas.create_text(x, y, text=str(self.board[i][j]), tags=f"numbers {i}-{j}", font=("Arial", 32))
        self.draw_grid()

    def draw_grid(self):
        logging.debug("Drawing grid.")
        for i in range(10):
            width = 3 if i % 3 == 0 else 1
            self.canvas.create_line(10 + i * 60, 10, 10 + i * 60, 550, tags="grid", width=width)
            self.canvas.create_line(10, 10 + i * 60, 550, 10 + i * 60, tags="grid", width=width)

    def select_cell(self, event):
        logging.debug("Selecting cell.")
        col, row = (event.x - 10) // 60, (event.y - 10) // 60
        if (row, col) not in self.fixed_cells:
            self.canvas.delete("highlight")
            self.selected_cell = (row, col)
            self.canvas.create_rectangle(10 + 60 * col, 10 + 60 * row, 70 + 60 * col, 70 + 60 * row, fill="yellow", tags="highlight")
            self.root.bind("<Key>", self.key_press)

    def key_press(self, event):
        self.unique_counter += 1  # Use class variable
        logging.debug("Attempting to insert number.")
        if self.selected_cell and event.char in "123456789":
            row, col = self.selected_cell
            if (row, col) in self.fixed_cells:
                logging.debug("Cell is fixed. Skipping.")
                return
            num = int(event.char)
            x, y = 40 + col * 60, 40 + row * 60
            unique_tag = f"numbers {row}-{col}-{self.unique_counter}"
            self.canvas.delete(f"numbers {row}-{col}-*")
            if num == self.solved_board[row][col]:
                logging.debug(f"Inserting correct number {num} at ({row}, {col}) with tag {unique_tag}.")
                self.canvas.create_text(x, y, text=str(num), tags=unique_tag, fill="green", font=("Arial", 32))
                self.board[row][col] = num
                self.fixed_cells.add((row, col))
            else:
                logging.debug(f"Inserting incorrect number {num} at ({row}, {col}) with tag {unique_tag}.")
                self.canvas.create_text(x, y, text=str(num), tags=unique_tag, fill="red", font=("Arial", 32))

    def hint(self):
        logging.debug("Providing hint.")
        if self.selected_cell:
            row, col = self.selected_cell
            hint_value = self.solved_board[row][col]
            if hint_value == 0:
                return
            x, y = 40 + col * 60, 40 + row * 60
            self.canvas.delete(f"numbers {row}-{col}")
            self.canvas.create_text(x, y, text=str(hint_value), tags=f"numbers {row}-{col}", fill="blue", font=("Arial", 32))
            self.board[row][col] = hint_value
            self.fixed_cells.add((row, col))

if __name__ == "__main__":
    root = tk.Tk()
    sudoku = Sudoku(root)
    root.mainloop()
