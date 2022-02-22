import sys
input = sys.stdin.readline

N = int(input())

count = [0]*10001
for _ in range(N):
    count[int(input())] += 1

for i in range(1, 10001):
    while count[i] > 0:
        print(i)
        count[i] -= 1




"""
lst = [int(input()) for _ in range(N)]

#Counting Sort 사용
count = [0] * (max(lst)+1)

for i in lst:
    count[i] += 1

num = count[1]
for i in range(2, len(count)):
    count[i] += num
    num = count[i]

result = [0] * (len(lst)+1)
for i in reversed(lst):
    result[count[i]] = i
    count[i] -= 1

for i in range(1, len(result)):
    print(result[i])
"""