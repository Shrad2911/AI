# N-Queens Problem

N = int(input("Enter value of N: "))

#Creates list to store queen positions.-1 means queen not placed yet.
board = [-1] * N  

# Check safe position
def isSafe(row, col):

    for i in range(row):

        # Same column
        if board[i] == col:
            return False

        # Diagonal check
        if abs(board[i] - col) == abs(i - row):
            return False

    return True

# Solve using backtracking
def solve(row):

    # All queens placed
    if row == N:
        return True

    # Try every column
    for col in range(N):

        if isSafe(row, col):

            board[row] = col

            if solve(row + 1):
                return True

    return False
# Print board
def printBoard():

    for i in range(N):

        for j in range(N):

            if board[i] == j:
                print("Q", end=" ")
            else:
                print(".", end=" ")

        print()
# Main
if solve(0):

    print("\nSolution Exists:\n")
    printBoard()

else:
    print("No Solution Exists")


-->The N-Queens problem places N queens on an N × N chessboard so that
A queen can attack:No two queens should be in:
Same row
Same column
Same diagonal
Technique used: Backtracking.
Time Complexity:O(N!)
Space Complexity:O(N)
