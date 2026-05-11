# DFS and BFS Traversal using Menu Driven Program

from collections import deque

graph = {}
visited = set()


# DFS Recursive Function
def DFS(node):
    visited.add(node)
    print(node, end=" ")

    for neighbor in graph[node]:
        if neighbor not in visited:
            DFS(neighbor)


# BFS Function
def BFS(start):
    bfs_visited = set()
    queue = deque()

    bfs_visited.add(start)
    queue.append(start)

    while queue:
        node = queue.popleft()
        print(node, end=" ")

        for neighbor in graph[node]:
            if neighbor not in bfs_visited:
                bfs_visited.add(neighbor)
                queue.append(neighbor)


# Main Program
V = int(input("Enter number of vertices: "))

# Create empty graph
for i in range(V):
    graph[i] = []

while True:
    print("\n--- MENU ---")
    print("1. Add Edge")
    print("2. Display Graph")
    print("3. DFS Traversal")
    print("4. BFS Traversal")
    print("5. Exit")

    choice = int(input("Enter Choice: "))

    # Add Edge
    if choice == 1:
        u = int(input("Enter source vertex: "))
        v = int(input("Enter destination vertex: "))

        graph[u].append(v)
        graph[v].append(u)   # Undirected Graph

    # Display Graph
    elif choice == 2:
        print("Graph:")

        for node in graph:
            print(node, "->", end=" ")

            for neighbor in graph[node]:
                print(neighbor, end=" ")

            print()

    # DFS
    elif choice == 3:
        visited.clear()

        start = int(input("Enter starting vertex for DFS: "))

        print("DFS Traversal:")
        DFS(start)
        print()

    # BFS
    elif choice == 4:
        start = int(input("Enter starting vertex for BFS: "))

        print("BFS Traversal:")
        BFS(start)
        print()

    # Exit
    elif choice == 5:
        print("Exiting...")
        break

    else:
        print("Invalid Choice!")


DFS goes:
deep → deeper → deepest
Recursion helps program remember previous nodes automatically.
BFS visits:
Level by level
Uses a Queue to add and remove element
DFS → Stack / Recursion
 Why visited array is used?
To avoid:revisiting nodes,infinite loops
Time ComplexityFor both:O(V + E)
