n = int(input())
numbers = list(map(int, input().split()))
plus, minus, multiple, divide = map(int, input().split())

high = -1e9
low = 1e9
def dfs(result, cnt, plus, minus, multiple, divide):
    global high, low
    if cnt == n:
        high = max(result, high)
        low = min(result, low)
        return

    if plus:
        dfs(result + numbers[cnt], cnt+1, plus-1, minus, multiple, divide)
    if minus:
        dfs(result - numbers[cnt], cnt+1, plus, minus-1, multiple, divide)
    if multiple:
        dfs(result * numbers[cnt], cnt+1, plus, minus, multiple-1, divide)
    if divide:
        dfs(int(result / numbers[cnt]), cnt+1, plus, minus, multiple, divide-1)

dfs(numbers[0], 1, plus, minus, multiple, divide)
print(high)
print(low)