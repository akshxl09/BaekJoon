from itertools import combinations
n,m = map(int, input().split())

lst = [i for i in range(1, n+1)]

for com in combinations(lst, m):
    print(' '.join(map(str, com)))