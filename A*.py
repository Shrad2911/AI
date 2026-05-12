import heapq

class Node:
    def __init__(self, x, y, g, h, parent=None):
        self.x = x
        self.y = y
        self.g = g          # Cost from start
        self.h = h          # Heuristic value
        self.f = g + h      # Total cost
        self.parent = parent
#This is a special function in Python called: lt means:less than
    def __lt__(self, other):
        return self.f < other.f


# Heuristic Function (Manhattan Distance)
def heuristic(x1, y1, x2, y2):
    return abs(x1 - x2) + abs(y1 - y2)


# Input rows and columns
rows = int(input("Enter number of rows: "))
cols = int(input("Enter number of cols: "))

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

# Priority Queue
open_list = []

# Visited array
visited = [[False for _ in range(cols)] for _ in range(rows)]

# Create start node
h = heuristic(sx, sy, gx, gy)

start = Node(sx, sy, 0, h)

heapq.heappush(open_list, start)

# Directions: up, down, left, right
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

found = False

while open_list:

    current = heapq.heappop(open_list)

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

    visited[current.x][current.y] = True

    # Check neighbors
    for i in range(4):

        nx = current.x + dx[i]
        ny = current.y + dy[i]

        if (0 <= nx < rows and
            0 <= ny < cols and
            maze[nx][ny] == 0 and
            not visited[nx][ny]):

            g = current.g + 1

            h = heuristic(nx, ny, gx, gy)

            neighbor = Node(nx, ny, g, h, current)

            heapq.heappush(open_list, neighbor)

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
heapq is a Python library used to create a Priority Queue.
(A* algorithm needs a priority queue to always select the node with the smallest cost.) A heap is a special tree-like data structure.
In Python, heapq creates a Min Heap.👉 Smallest value always comes first.
A* always chooses the node with smallest: f(n)=g(n)+h(n)So heap helps automatically sort nodes.
map():Apply the same function to every element one by one.    
A* is an informed search algorithm used to find the shortest path.f(n)=g(n)+h(n)
g(n) = actual cost from start,h(n) = estimated cost to goal,f(n) = total cost
data structure is used? Priority Queue using heapq
A* uses heuristic values, so it reaches the goal faster.
A* algorithm is better because it finds shortest path faster using heuristic function.”
BFS is better for shortest path because DFS may go into wrong deep path.”(It explores nearby nodes level by level.)
DFS is simplest and easiest to implement.”
A* algorithm is widely used in games and navigation systems.
     Time	Space 
BFS	O(V+E)	O(V)
DFS	O(V+E)	O(V)
A*	O(E)good	O(V)
