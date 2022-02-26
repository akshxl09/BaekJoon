n,m = map(int, input().split())
answer = []
def dfs(lst, cnt, string):
    if cnt >= m:
        answer.append(string)
        return
    
    for i in range(n):
        if not visited[i]:
            visited[i] = 1
            dfs(lst, cnt+1, string + str(lst[i]))
            visited[i] = 0

lst = [i for i in range(1, n+1)]
visited = [0] * n

dfs(lst, 0, '')
for num in answer:
    print(' '.join(num))


'''
from itertools import permutations
n, m = map(int, input().split())

lst = [i for i in range(1, n+1)]

for per in permutations(lst, m):
    print(' '.join(map(str, per)))
'''