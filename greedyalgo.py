# Greedy Algorithms Menu Program
# 1. Selection Sort
# 2. Prim's Algorithm
# 3. Job Scheduling Problem

import heapq

# ---------------- Selection Sort ----------------
def selection_sort():

    arr = list(map(int, input("Enter array elements: ").split()))

    n = len(arr)

    for i in range(n):

        min_index = i

        for j in range(i + 1, n):

            if arr[j] < arr[min_index]:
                min_index = j

        arr[i], arr[min_index] = arr[min_index], arr[i]

    print("\nSorted Array:")
    print(arr)


# ---------------- Prim's Algorithm ----------------
def prims_algorithm():

    graph = {
        'A': [('B', 1), ('C', 4)],
        'B': [('A', 1), ('C', 2), ('D', 5)],
        'C': [('A', 4), ('B', 2), ('D', 1)],
        'D': [('B', 5), ('C', 1)]
    }

    start = input("Enter starting node: ")

    visited = set()

    min_heap = [(0, start, None)]

    total_cost = 0

    print("\nEdges in Minimum Spanning Tree:")

    while min_heap:

        weight, node, parent = heapq.heappop(min_heap)

        if node not in visited:

            visited.add(node)

            total_cost += weight

            if parent is not None:
                print(parent, "-", node, "=", weight)

            for neighbor, cost in graph[node]:

                if neighbor not in visited:
                    heapq.heappush(min_heap, (cost, neighbor, node))

    print("\nTotal Minimum Cost =", total_cost)


# ---------------- Job Scheduling ----------------
def job_scheduling():

    jobs = []

    n = int(input("Enter number of jobs: "))

    for i in range(n):

        print("\nJob", i + 1)

        name = input("Enter Job Name: ")
        deadline = int(input("Enter Deadline: "))
        profit = int(input("Enter Profit: "))

        jobs.append((name, deadline, profit))

    # Sort jobs by profit
    jobs.sort(key=lambda x: x[2], reverse=True)

    max_deadline = max(job[1] for job in jobs)

    slots = [False] * max_deadline

    selected_jobs = []

    total_profit = 0

    for job in jobs:

        name, deadline, profit = job

        for j in range(deadline - 1, -1, -1):

            if slots[j] == False:

                slots[j] = True

                selected_jobs.append(name)

                total_profit += profit

                break

    print("\nSelected Jobs:", selected_jobs)

    print("Total Profit:", total_profit)


# ---------------- Main Menu ----------------
while True:

    print("\n----- GREEDY ALGORITHMS MENU -----")

    print("1. Selection Sort")
    print("2. Prim's Algorithm")
    print("3. Job Scheduling Problem")
    print("4. Exit")

    choice = int(input("Enter your choice: "))

    if choice == 1:
        selection_sort()

    elif choice == 2:
        prims_algorithm()

    elif choice == 3:
        job_scheduling()

    elif choice == 4:
        print("Program Ended")
        break

    else:
        print("Invalid Choice")

  ----- GREEDY ALGORITHMS MENU -----
1. Selection Sort
2. Prim's Algorithm
3. Job Scheduling Problem
4. Exit
Enter your choice: 1
Enter array elements: 2 1 4 3 8 5

Sorted Array:
[1, 2, 3, 4, 5, 8]

----- GREEDY ALGORITHMS MENU -----
1. Selection Sort
2. Prim's Algorithm
3. Job Scheduling Problem
4. Exit
Enter your choice: 2
Enter starting node: A

Edges in Minimum Spanning Tree:
A - B = 1
B - C = 2
C - D = 1

Total Minimum Cost = 4

----- GREEDY ALGORITHMS MENU -----
1. Selection Sort
2. Prim's Algorithm
3. Job Scheduling Problem
4. Exit
Enter your choice: 3
Enter number of jobs: 2

Job 1
Enter Job Name: j1
Enter Deadline: 2
Enter Profit: 50

Job 2
Enter Job Name: j2
Enter Deadline: 1
Enter Profit: 30

Selected Jobs: ['j1', 'j2']
Total Profit: 80

concept:A Greedy Algorithm solves a problem by choosing the best option at the current step without worrying about future steps.
It tries to find an optimal solution quickly.
->Selection Sort repeatedly finds the smallest element from the unsorted part and places it at the beginning.
It is called greedy because in every step it selects the minimum element.
->Prim’s algorithm starts from one node and keeps adding the minimum edge.
Steps Uses priority queue (heap)
Start from any vertex
Select minimum edge
Add new vertex
Repeat until all vertices are included
	             Time 	       Space 
Selection Sort	O(n²)       	O(1)
Prim’s Algorithm	O(E log V)	O(V + E)
Job Scheduling	O(n²)        	O(n)

Selection Sort → Nested loops → O(n²)
Prim → Heap + Graph → O(E log V)
Job Scheduling → Sorting + slots → O(n²)


