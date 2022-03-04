n = int(input())
lst = []
for _ in range(n):
    lst.append(list(map(int,input())))
    
cnt = 0
def dfs(i,j):
    global cnt
    if (i < 0 or i >= n) or ( j < 0 or j >= n):
        return
    if lst[i][j] == 0:
        return

    cnt += 1
    lst[i][j] = 0

    dfs(i-1, j)
    dfs(i+1, j)
    dfs(i, j-1)
    dfs(i, j+1)


answer = []
for i in range(n):
    for j in range(n):
        if lst[i][j] == 1:
            dfs(i,j)
            answer.append(cnt)
            cnt = 0

print(len(answer))
for i in sorted(answer):
    print(i)