
def floyd_warshall():
    
    n = int(input("Enter the number of nodes: "))
    m = int(input("Enter the number of edges: "))

    
    INF = float('inf')
    dist = [[INF] * n for _ in range(n)]

    
    for i in range(n):
        dist[i][i] = 0

    
    print("Enter edges in the format 'u v w' (1-based indices):")
    for _ in range(m):
        u, v, w = map(int, input().split())
        dist[u - 1][v - 1] = w

    
    for k in range(n):
        for i in range(n):
            for j in range(n):
                dist[i][j] = min(dist[i][j], dist[i][k] + dist[k][j])

    
    start = int(input("Enter the starting node (1-based index): ")) - 1

    
    min_cost = 0
    unreachable = False
    for i in range(n):
        if dist[start][i] == INF:
            unreachable = True
        else:
            min_cost += dist[start][i]

    
    if unreachable:
        print("Some nodes are unreachable from the starting node.")
    else:
        print(f"The minimum cost to cover all nodes from node {start + 1} is: {min_cost}")



floyd_warshall()
