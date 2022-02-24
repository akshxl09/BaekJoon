import sys
input = sys.stdin.readline

N = int(input())

lst = [list(map(int, input().split())) for _ in range(N)]

lst = sorted(lst, key=lambda x: (x[1], x[0]))

answer = 0
time = 0
for i in range(N):
    if lst[i][0] >= time:
        answer += 1
        time = lst[i][1]

print(answer)
