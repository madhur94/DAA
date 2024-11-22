def floyd_warshall():
    
    n = int(input("ENter the number of nodes: "))
    m = int(input("ENter the number of edges: "))
    
    INF  = float('inf')
    dist = [[INF]*n for _ in range(n)]
    
    for i in range(n):
        dist[i][i] = 0
        
    print(f"Enter in following format u v w : ")
    for _ in range(m):
        u,v,w = map(int,input().split())
        dist[u-1][v-1] = w
        
    for k in range(n):
        for i in range(n):
            for j in range(n):
                dist[i][j] = min(dist[i][j],dist[i][k]+dist[k][j])
    
    print("Enter the starting node")
                    