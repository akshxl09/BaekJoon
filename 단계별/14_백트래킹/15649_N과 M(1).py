n,m = map(int, input().split())
answer = []
def dfs(cnt, string):
    if cnt >= m:
        answer.append(string)
        return
    
    for i in range(0,n):
        if not visited[i]:
            visited[i] = 1
            dfs(cnt+1, string + str(i+1))
            visited[i] = 0

visited = [0] * n

dfs(0, '')
for num in answer:
    print(' '.join(num))


'''
from itertools import permutations
n, m = map(int, input().split())

lst = [i for i in range(1, n+1)]

for per in permutations(lst, m):
    print(' '.join(map(str, per)))
'''