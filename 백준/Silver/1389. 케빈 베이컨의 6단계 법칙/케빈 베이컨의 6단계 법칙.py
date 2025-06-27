"""
케빈 베이컨의 6단계 법칙
케빈 베이컨 게임 : 임의의 두 사람이 최소 몇 단계 만에 이어질 수 있는 지 계산
케빈 베이컨은 모든 사람에게 이어지는 수만큼
결과 ->  케빈 베이컨 수가 가장 작은 사람 출력


"""

N, M = map(int, input().split())
# 친구 관계의 수
friends_list = [0] * N
INF = int(1e9)
graph = [[INF] * (N + 1) for _ in range(N + 1)]
for _ in range(M):
    a, b = map(int, input().split())
    graph[a][b] = 1
    graph[b][a] = 1

for idx in range(1, N + 1):
    for jdx in range(1, N + 1):
        if idx == jdx:
            graph[idx][jdx] = 0

for kdx in range(1, N + 1):
    for idx in range(1, N + 1):
        for jdx in range(1, N + 1):
            graph[idx][jdx] = min(graph[idx][jdx], graph[idx][kdx] + graph[kdx][jdx])

min_value = INF
result = 0
# n번째 행의 합이 제일 적은 사람
for idx in range(1, N + 1):
    s = sum(graph[idx][1:])
    if min_value > s:
        min_value = s
        result = idx

print(result)