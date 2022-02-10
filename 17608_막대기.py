import sys
input = sys.stdin.readline
N = int(input())

arr = [int(input()) for i in range(N)]

result = 1
max = arr[N-1]
for i in range(N-2, -1, -1):
    if arr[i] > max:
        result += 1
        max = arr[i]
print(result)