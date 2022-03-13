n = int(input())

s = [list(map(int,input().split())) for _ in range(n)]

people = [x for x in range(n)]
visited = [0] * n

low = 1e9
def dfs(visited, team, k):
    global low
    if len(team) == n//2:
        other = []
        for i in people:
            if i not in team:
                other.append(i)
        result_1 = 0
        result_2 = 0
        for i in range(n//2):
            for j in range(n//2):
                if i != j:
                    result_1 += s[team[i]][team[j]]
                    result_2 += s[other[i]][other[j]]

        low = min(low, abs(result_1 - result_2))

        return

    for i in range(k, n):
        if not  visited[i]:
            visited[i] = 1
            team.append(people[i])
            dfs(visited, team, i)
            team.pop()
            visited[i] = 0

dfs(visited, [], 0)
print(low)