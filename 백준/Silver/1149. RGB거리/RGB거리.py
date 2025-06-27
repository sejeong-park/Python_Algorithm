"""
RGB거리
- 1번 - N번 순서대로
- 빨, 초, 파 -> 하나의 색으로 칠해야한다.

"""

N = int(input().strip())
matrix = [list(map(int, input().split())) for _ in range(N)]
for idx in range(1, N):
    matrix[idx][0] += min(matrix[idx - 1][1], matrix[idx - 1][2])
    matrix[idx][1] += min(matrix[idx - 1][0], matrix[idx - 1][2])
    matrix[idx][2] += min(matrix[idx - 1][1], matrix[idx - 1][0])

result = 1e9
for idx in range(3):
    result = min(result, matrix[N - 1][idx])

print(result)