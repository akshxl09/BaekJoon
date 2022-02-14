M, N = map(int, input().split())

lst = []
for i in range(M):
    lst.append(list(input()))

row = 0
col = 0
answer = []
while row < M - 7:
    cnt = 0

    for i in range(row, row + 8):
        for j in range(col, col + 8):
            if i==row and j==col: continue
            if (row+col)%2 == (i+j)%2:
                if lst[row][col] != lst[i][j]:
                    cnt += 1
            else:
                if lst[row][col] == lst[i][j]:
                    cnt += 1

    answer.append(cnt) 

    col += 1
    if col >= N - 7:
        col = 0
        row += 1

print(len(answer))
print(answer)
print(min(answer))