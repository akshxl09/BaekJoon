answer = set()
N = int(input())
num = list(input().replace(" ", ""))

def solution(left, right, i):
    answer.add(abs(left-right))
    if i == N: return

    solution(left + int(num[i]), right, i + 1)
    solution(left, right + int(num[i]), i + 1)
    solution(left, right, i + 1)

solution(0, 0, 0)
print(sum(map(int, num))- len(answer) + 1)