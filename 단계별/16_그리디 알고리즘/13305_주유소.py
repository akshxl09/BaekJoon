N = int(input())
distance = list(map(int, input().split())) + [0]
gas = list(map(int, input().split()))

price = gas[0]
dis = 0
result = 0
for i in range(N):
    if price > gas[i]:
        result += price * dis
        dis = distance[i]
        price = gas[i]
    else:
        dis += distance[i]

if dis:
    result += price * dis

print(result)