from collections import deque
n, m, v = map(int, input().split())

def dfs(edge,visited, v):
    if visited[v]:
        return

    print(v, end=" ")
    visited[v] = 1
    for lst in edge:
        if v in lst and not visited[lst[(1-lst.index(v))%2]]:
            dfs(edge, visited, lst[(1-lst.index(v))%2])

def bfs(edge, visited, v):
    queue = deque([v])
    visited[v] = 1

    while(queue):
        for lst in edge:
            if queue[0] in lst and not visited[lst[(1-lst.index(queue[0]))%2]]:
                visited[lst[(1-lst.index(queue[0]))%2]] = 1
                queue.append(lst[(1-lst.index(queue[0]))%2])
        print(queue.popleft(), end=" ")
            
visited = [0]*(n+1)

edge = []
for i in range(m):
    a, b = map(int, input().split())
    if b < a:
        a, b = b, a
    edge.append([a,b])

dfs(sorted(edge), visited, v)
print()
visited = [0] * (n+1)
bfs(sorted(edge), visited, v)