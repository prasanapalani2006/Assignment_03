# Prim's Algorithm – Minimum Spanning Tree

## Description

This project implements **Prim's Algorithm** in Python to find the **Minimum Spanning Tree (MST)** of a weighted, undirected graph.

The program starts from a specified node and repeatedly selects the minimum-weight edge that connects a visited node to an unvisited node. It finally returns the total weight of the MST.

## Algorithm

1. Read the number of vertices and edges.
2. Store the graph using an adjacency list.
3. Start Prim's Algorithm from the given starting node.
4. Use a **min-heap (priority queue)** to select the smallest available edge.
5. Mark each selected vertex as visited.
6. Add the selected edge weight to the total.
7. Continue until all vertices are included.
8. Print the total MST weight.

## Input Format

```text
n m
u v w
u v w
...
start
```

- `n` – Number of nodes.
- `m` – Number of edges.
- `u v w` – An edge between nodes `u` and `v` with weight `w`.
- `start` – Starting node for Prim's Algorithm.

## Sample Input

```text
5 6
1 2 3
1 3 4
4 2 6
5 2 2
2 3 5
3 5 7
1
```

## Sample Output

```text
15
```

## Explanation

Starting from node `1`, Prim's Algorithm selects the minimum-weight edges while ensuring that no cycle is formed.

Selected edges:

- `1 → 2` with weight `3`
- `2 → 5` with weight `2`
- `1 → 3` with weight `4`
- `2 → 4` with weight `6`

Total MST weight:

```text
3 + 2 + 4 + 6 = 15
```

## Complexity

- **Time Complexity:** `O(E log V)`
- **Space Complexity:** `O(V + E)`

where `V` is the number of vertices and `E` is the number of edges.

## Requirements

- Python 3.x
- No external libraries are required.
- The program uses Python's built-in `heapq` module.

## File

The main Python program contains the `prims()` function and input/output handling. The graph is represented using an adjacency list and the priority queue is implemented using `heapq`. fileciteturn0file0L3-L12

## How to Run

```bash
python prims.py
```

Enter the input according to the specified format.

## Author

Student Project – Prim's Algorithm
