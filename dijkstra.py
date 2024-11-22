import heapq
from collections import defaultdict

def network_delay_time():
    # Input the number of nodes and edges
    n = int(input("Enter the number of nodes (N): "))
    m = int(input("Enter the number of edges (M): "))

    # Build the graph as an adjacency list
    graph = defaultdict(list)
    print("Enter edges in the format 'u v w' (1-based indices):")
    for _ in range(m):
        u, v, w = map(int, input().split())
        graph[u].append((v, w))

    # Input the starting node
    k = int(input("Enter the starting node (K): "))

    # Dijkstra's algorithm to find the shortest times
    min_time = {i: float('inf') for i in range(1, n + 1)}
    min_time[k] = 0
    priority_queue = [(0, k)]  # (current_time, node)

    while priority_queue:
        current_time, current_node = heapq.heappop(priority_queue)

        if current_time > min_time[current_node]:
            continue

        for neighbor, weight in graph[current_node]:
            time = current_time + weight
            if time < min_time[neighbor]:
                min_time[neighbor] = time
                heapq.heappush(priority_queue, (time, neighbor))

    # Calculate the maximum time to reach all nodes
    max_time = max(min_time.values())
    print(max_time if max_time != float('inf') else -1)


# Run the function
network_delay_time()
 