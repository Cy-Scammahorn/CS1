import random

#Prints the Sudoku with boarders
def print_sudoku(board):
    for i in range(9):
        if i % 3 == 0:
            print("+-------+-------+-------+")
        for j in range(9):
            if j % 3 == 0:
                print("|", end=" ")
            print(board[i][j] if board[i][j] != 0 else ".", end=" ")
        print("|")
    print("+-------+-------+-------+")


# This step finds the first empty cell that needs to be filled
def find_empty(board):
    for i in range(9):
        for j in range(9):
            if board[i][j] == 0:
                return i, j
    return None


# This checks if the number in the board is a vaild number 
def is_valid(board, num, pos):
    row, col = pos
    # This will Check the row
    for j in range(9):
        if board[row][j] == num:
            return False
    # This will check the column
    for i in range(9):
        if board[i][col] == num:
            return False
    # This will check the 3x3 box
    box_row, box_col = row // 3, col // 3
    for i in range(box_row*3, box_row*3+3):
        for j in range(box_col*3, box_col*3+3):
            if board[i][j] == num:
                return False
    return True


# ---------- Backtracking Solver ----------
def solve(board):
    empty = find_empty(board)
    if not empty:
        return True
    row, col = empty
    for num in range(1, 10):
        if is_valid(board, num, (row, col)):
            board[row][col] = num
            if solve(board):
                return True
            board[row][col] = 0  # Backtrack
    return False


# ---------- Randomize a Solved Board ----------
def shuffle_board(board):
    new_board = [row[:] for row in board]

    # Swap rows within each 3x3 box
    for box in range(3):
        rows = list(range(box*3, box*3+3))
        random.shuffle(rows)
        new_board[box*3:box*3+3] = [new_board[r] for r in rows]

    # Swap columns within each 3x3 box
    for box in range(3):
        cols = list(range(box*3, box*3+3))
        random.shuffle(cols)
        for row in new_board:
            row[box*3:box*3+3] = [row[c] for c in cols]

    # Swap numbers globally
    numbers = list(range(1, 10))
    shuffled_numbers = numbers[:]
    random.shuffle(shuffled_numbers)
    mapping = {numbers[i]: shuffled_numbers[i] for i in range(9)}
    for i in range(9):
        for j in range(9):
            new_board[i][j] = mapping[new_board[i][j]]

    return new_board


# ---------- Make Puzzle by Removing Numbers ----------
def make_puzzle(board, empties=40):
    puzzle = [row[:] for row in board]
    count = 0
    while count < empties:
        i, j = random.randint(0,8), random.randint(0,8)
        if puzzle[i][j] != 0:
            puzzle[i][j] = 0
            count += 1
    return puzzle


# ---------- Base Solved Board ----------
solved_board = [
    [5,3,4,6,7,8,9,1,2],
    [6,7,2,1,9,5,3,4,8],
    [1,9,8,3,4,2,5,6,7],
    [8,5,9,7,6,1,4,2,3],
    [4,2,6,8,5,3,7,9,1],
    [7,1,3,9,2,4,8,5,6],
    [9,6,1,5,3,7,2,8,4],
    [2,8,7,4,1,9,6,3,5],
    [3,4,5,2,8,6,1,7,9]
]

# ---------- Generate Random Puzzle ----------
random_solved = shuffle_board(solved_board)
current_puzzle = make_puzzle(random_solved, empties=40)

print("Here's your Sudoku puzzle:")
print_sudoku(current_puzzle)

# ---------- Interactive loop ----------
while True:
    user_input = input("Type 'solve' to solve, 'new' for a new puzzle, or 'quit' to exit: ").strip().lower()
    
    if user_input == "solve":
        puzzle_copy = [row[:] for row in current_puzzle]  # copy to solve
        if solve(puzzle_copy):
            print("\nSolved Sudoku:")
            print_sudoku(puzzle_copy)
        else:
            print("No solution exists!")
            
    elif user_input == "new":
        random_solved = shuffle_board(solved_board)
        current_puzzle = make_puzzle(random_solved, empties=40)
        print("\nHere's a new Sudoku puzzle:")
        print_sudoku(current_puzzle)
        
    elif user_input == "quit":
        print("Goodbye!")
        break
        
    else:
        print("Invalid input! Type 'solve', 'new', or 'quit'.")
