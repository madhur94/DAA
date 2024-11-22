
def floyd_warshall():
    # Input the number of nodes and edges
    n = int(input("Enter the number of nodes: "))
    m = int(input("Enter the number of edges: "))

    # Initialize the distance matrix
    INF = float('inf')
    dist = [[INF] * n for _ in range(n)]

    # Distance to self is 0
    for i in range(n):
        dist[i][i] = 0

    # Input edges
    print("Enter edges in the format 'u v w' (1-based indices):")
    for _ in range(m):
        u, v, w = map(int, input().split())
        dist[u - 1][v - 1] = w  # Convert to 0-based index

    # Floyd-Warshall algorithm
    for k in range(n):
        for i in range(n):
            for j in range(n):
                dist[i][j] = min(dist[i][j], dist[i][k] + dist[k][j])

    # Ask for the starting node
    start = int(input("Enter the starting node (1-based index): ")) - 1

    # Calculate the minimum cost to cover all nodes from the starting node
    min_cost = 0
    unreachable = False
    for i in range(n):
        if dist[start][i] == INF:
            unreachable = True
        else:
            min_cost += dist[start][i]

    # Output the result
    if unreachable:
        print("Some nodes are unreachable from the starting node.")
    else:
        print(f"The minimum cost to cover all nodes from node {start + 1} is: {min_cost}")


# Run the function
floyd_warshall()
