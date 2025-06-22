from collections import deque
# 가로 : N / 세로 M
N, M = map(int, input().split())
matrix = [list(input().strip()) for _ in range(M)]
visited = [[False] * N for _ in range(M)]

def bfs(x, y):
    queue = deque([(x, y)])
    visited[y][x] = True
    count = 1
    color = matrix[y][x] # 색상

    dx = [0, 0, -1, 1]
    dy = [-1, 1, 0, 0]

    while queue:
        x, y = queue.popleft()

        for idx in range(4):
            nx = x + dx[idx]
            ny = y + dy[idx]

            if 0 <= nx < N and 0 <= ny < M:
                if matrix[ny][nx] == color and not visited[ny][nx]:
                    queue.append((nx, ny))
                    visited[ny][nx] = True
                    count += 1

    return count

blue_team, white_team = 0, 0
for y in range(M):
    for x in range(N):
        if not visited[y][x]:
            count = bfs(x, y)
            size = count ** 2

            if matrix[y][x] == "B":
                blue_team += size
            else:
                white_team += size

print(white_team, blue_team)