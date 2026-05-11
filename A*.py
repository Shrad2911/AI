from collections import deque

class Node:
    def __init__(self, x, y, parent=None):
        self.x = x
        self.y = y
        self.parent = parent

# Input rows and columns
rows = int(input("Enter rows: "))
cols = int(input("Enter cols: "))

# Input maze
maze = []

print("Enter maze (0=path, 1=wall):")

for i in range(rows):
    row = list(map(int, input().split()))
    maze.append(row)

# Start position
sx, sy = map(int, input("Enter start x y: ").split())

# Goal position
gx, gy = map(int, input("Enter goal x y: ").split())

# Queue for search
q = deque()

visited = [[False for _ in range(cols)] for _ in range(rows)]

# Add start node
q.append(Node(sx, sy))
visited[sx][sy] = True

# Directions: up, down, left, right
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

found = False

while q:

    current = q.popleft()

    # Goal reached
    if current.x == gx and current.y == gy:

        print("\nPath Found:")

        path = []

        while current:
            path.append((current.x, current.y))
            current = current.parent

        path.reverse()

        for p in path:
            print(p)

        found = True
        break

    # Check neighbors
    for i in range(4):

        nx = current.x + dx[i]
        ny = current.y + dy[i]

        if (0 <= nx < rows and
            0 <= ny < cols and
            maze[nx][ny] == 0 and
            not visited[nx][ny]):

            visited[nx][ny] = True
            q.append(Node(nx, ny, current))

if not found:
    print("No Path Found")

output:Enter rows: 3
Enter cols: 3
Enter maze (0=path, 1=wall):
0 0 1
0 1 0
0 0 0
Enter start x y: 0 0
Enter goal x y: 2 2

Path Found:
(0, 0)
(1, 0)
(2, 0)
(2, 1)
(2, 2)

deque is used to create a queue.
It follows FIFO (First In First Out).
It is used to store positions during searching.
What is self?
self represents the current object of the class.
It is used to access variables inside the class.
Example:self.x
means current object's x value.
split() separates input using spaces.
map() converts data type.map(int, input().split())
converts string values into integers.
list() converts values into list format.popleft() removes first element from queue.
Node represents one position in maze/game.
Example:(1,2)is one node.
0 <= nx < rows
Checks if position is inside maze.
What does maze[nx][ny] == 0 mean?
Checks whether path is free.
A* algorithm is better because it finds shortest path faster using heuristic function.”
BFS is better for shortest path because DFS may go into wrong deep path.”(It explores nearby nodes level by level.)
DFS is simplest and easiest to implement.”
A* algorithm is widely used in games and navigation systems.
     Time	Space 
BFS	O(V+E)	O(V)
DFS	O(V+E)	O(V)
A*	O(E)good	O(V)
