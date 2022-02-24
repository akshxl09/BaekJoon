N = int(input())
lst = list(map(int, input().split()))

lst = sorted(lst)

answer = 0
result = 0
for i in lst:
    answer += i
    result += answer

print(result)