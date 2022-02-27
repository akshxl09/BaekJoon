n,m = map(int, input().split())

def dfs(lst, k, answer):
    if sum(visited) >= m:
        print(' '.join(answer))
        return
    
    for i in range(k, n): #k가 포인트!
        if not visited[i]:
            visited[i] = 1
            dfs(lst, i, answer + str(lst[i]))
            visited[i] = 0

lst = [i for i in range(1, n+1)]
visited = [0] * n

dfs(lst, 0, '')


'''
from itertools import combinations
n,m = map(int, input().split())

lst = [i for i in range(1, n+1)]

for com in combinations(lst, m):
    print(' '.join(map(str, com)))
'''