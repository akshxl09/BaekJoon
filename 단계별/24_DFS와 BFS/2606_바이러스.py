from collections import defaultdict, deque

graph = defaultdict(list)
n = int(input())
m = int(input())

for _ in range(m):
    a, b = map(int,input().split())
    graph[a].append(b)
    graph[b].append(a)


queue = deque([1])
visited = [0] * (n+1)

answer = 0
while queue:
    v = queue.popleft()
    for i in graph[v]:
        if not visited[i]:
            answer += 1
            visited[i] = 1
            queue.append(i)

print(answer-1)