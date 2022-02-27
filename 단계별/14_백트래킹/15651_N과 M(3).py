n,m = map(int, input().split())

def dfs(lst, answer, cnt):
    if cnt == m:
        print(' '.join(answer))
        return
    
    for i in range(n):
        dfs(lst, answer + str(lst[i]), cnt + 1)
        


lst = [i for i in range(1,n+1)]

dfs(lst, '', 0)


'''
from itertools import product
n,m = map(int, input().split())

lst = [i for i in range(1, n+1)]

for pro in product(lst, repeat=m):
    print(' '.join(map(str, pro)))
'''