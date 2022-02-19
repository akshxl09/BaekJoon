N, K = map(int, input().split())

lst = [int(input()) for _ in range(N)]

cnt = 0

for coin in reversed(lst):
    num = K//coin
    if num >= 1:
        K -= num*coin
        cnt += num
        
print(cnt)