M, N = map(int, input().split())

lst = []
for i in range(M):
    lst.append(list(input()))

row = 0
col = 0
answer = []
while row < M - 7:
    cnt_b = 0
    cnt_w = 0

    for i in range(row, row + 8):
        for j in range(col, col + 8):
            if (row+col)%2 == (i+j)%2:
                if 'B' != lst[i][j]:
                    cnt_b += 1
            else:
                if 'B' == lst[i][j]:
                    cnt_b += 1
            
            if (row+col)%2 == (i+j)%2:
                if 'W' != lst[i][j]:
                    cnt_w += 1
            else:
                if 'W' == lst[i][j]:
                    cnt_w += 1

    answer.append(min(cnt_b, cnt_w)) 

    col += 1
    if col >= N - 7:
        col = 0
        row += 1

print(min(answer))

#w, b를 뭐로 판단하지?