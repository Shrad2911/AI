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
#graph coloring:
class GraphColoring:

    def __init__(self, graph):
        self.graph = graph
        self.V = len(graph)
        self.colors = [0] * self.V

        # Color names
        self.color_names = ["", "Red", "Green", "Blue", "Yellow", "Orange"]

    # Check whether current color can be assigned
    def is_safe(self, v, c):

        for i in range(self.V):

            # Adjacent vertex has same color
            if self.graph[v][i] == 1 and self.colors[i] == c:
                return False

        return True

    # Recursive function using Backtracking
    def solve_graph(self, v, m):

        # All vertices are colored
        if v == self.V:
            self.print_solution()
            return True

        # Try all colors one by one
        for c in range(1, m + 1):

            if self.is_safe(v, c):

                # Assign color
                self.colors[v] = c

                # Recur for next vertex
                if self.solve_graph(v + 1, m):
                    return True

                # Backtracking
                self.colors[v] = 0

        return False

    # Print final coloring solution
    def print_solution(self):

        print("\nSolution Exists!")
        print("Vertex -> Color")

        for i in range(self.V):
            print(f"{i} -> {self.color_names[self.colors[i]]}")

    # Main solve function
    def solve(self, m):

        if not self.solve_graph(0, m):
            print("\nNo solution exists")


# -------- DRIVER CODE --------

V = int(input("Enter number of vertices: "))

print("Enter adjacency matrix:")

graph = []

for i in range(V):
    row = list(map(int, input(f"Row {i+1}: ").split()))
    graph.append(row)

m = int(input("Enter number of colors: "))

gc = GraphColoring(graph)
gc.solve(m)
output:
Enter number of vertices: 3
Enter adjacency matrix:
Row 1: 0 1 1
Row 2: 1 0 1
Row 3: 1 1 0
Enter number of colors: 3

Solution Exists!
Vertex -> Color
0 -> Red
1 -> Green
2 -> Blue

We assign colors to graph vertices such that:

No two adjacent vertices have the same color
We try to use minimum constraints checking (pruning invalid choices early)

This is a classic CSP (Constraint Satisfaction Problem).
Backtracking
Try assigning colors one by one
If conflict occurs → undo and try another color
🔹 Branch and Bound (Pruning)
We reject a color immediately if:
Any adjacent vertex already has same color
This avoids exploring useless branches
Why CSP?
Variables → vertices
Domain → colors
Constraints → adjacent vertices must differ. Time Complexity?Worst case: O(m^V)(m = colors, V = vertices)
################## both in same #######################

# ---------------- N-QUEENS PROBLEM ----------------

class NQueens:

    def __init__(self, n):
        self.N = n

        # queens[i] = column position of queen in row i
        self.queens = [-1] * n

        # To check occupied columns
        self.column = [False] * n

        # Main diagonal
        self.diag1 = [False] * (2 * n - 1)

        # Secondary diagonal
        self.diag2 = [False] * (2 * n - 1)

    # Start solving
    def solve(self):

        if not self.place_queen(0):
            print("\nNo solution exists")

    # Recursive function
    def place_queen(self, row):

        # All queens placed
        if row == self.N:
            self.print_solution()
            return True

        # Try every column
        for col in range(self.N):

            # Check safety
            if (not self.column[col] and
                not self.diag1[row - col + self.N - 1] and
                not self.diag2[row + col]):

                # Place queen
                self.queens[row] = col

                self.column[col] = True
                self.diag1[row - col + self.N - 1] = True
                self.diag2[row + col] = True

                # Recur for next row
                if self.place_queen(row + 1):
                    return True

                # BACKTRACK
                self.queens[row] = -1
                self.column[col] = False
                self.diag1[row - col + self.N - 1] = False
                self.diag2[row + col] = False

        return False

    # Print board
    def print_solution(self):

        print("\nSolution Exists!\n")

        for i in range(self.N):

            for j in range(self.N):

                if self.queens[i] == j:
                    print("Q", end=" ")

                else:
                    print(".", end=" ")

            print()


# ---------------- GRAPH COLORING ----------------

class GraphColoring:

    def __init__(self, graph):

        self.graph = graph
        self.V = len(graph)

        # Color array
        self.colors = [0] * self.V

        self.color_names = [
            "", "Red", "Green",
            "Blue", "Yellow", "Orange"
        ]

    # Check whether color can be assigned
    def is_safe(self, v, c):

        for i in range(self.V):

            if self.graph[v][i] == 1 and self.colors[i] == c:
                return False

        return True

    # Recursive Backtracking
    def solve_graph(self, v, m):

        # All vertices colored
        if v == self.V:
            self.print_solution()
            return True

        # Try all colors
        for c in range(1, m + 1):

            if self.is_safe(v, c):

                # Assign color
                self.colors[v] = c

                # Recur for next vertex
                if self.solve_graph(v + 1, m):
                    return True

                # BACKTRACK
                self.colors[v] = 0

        return False

    # Print final solution
    def print_solution(self):

        print("\nSolution Exists!")
        print("Vertex -> Color")

        for i in range(self.V):

            print(
                f"{i} -> {self.color_names[self.colors[i]]}"
            )

    # Main function
    def solve(self, m):

        if not self.solve_graph(0, m):

            print("\nNo solution exists")


# ---------------- MAIN MENU ----------------

def main():

    while True:

        print("\n************* MAIN MENU **************")
        print("1. N-Queens Problem")
        print("2. Graph Coloring")
        print("3. Exit")

        choice = int(input("\nEnter your choice: "))

        # -------- N-QUEENS --------
        if choice == 1:

            n = int(input("Enter number of queens (N): "))

            q = NQueens(n)

            q.solve()

        # -------- GRAPH COLORING --------
        elif choice == 2:

            V = int(input("Enter number of vertices: "))

            print("\nEnter adjacency matrix:")

            graph = []

            for i in range(V):

                row = list(
                    map(int, input(f"Row {i+1}: ").split())
                )

                graph.append(row)

            m = int(input("Enter number of colors: "))

            gc = GraphColoring(graph)

            gc.solve(m)

        # -------- EXIT --------
        elif choice == 3:

            print("\nExiting Program...")
            break

        else:

            print("\nInvalid choice! Try again.")


# Driver Code
main()

