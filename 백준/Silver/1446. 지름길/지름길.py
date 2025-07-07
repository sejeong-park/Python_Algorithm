"""
지름길
"""

import sys
input = sys.stdin.readline

N, D = map(int, input().split())
shortcuts = []
for _ in range(N):
    start, end, length = map(int, input().split())
    # 고속도로 벗어나는 지름길 pass
    if end > D:
        continue
    # 지름길이 일반 도로보다 길면 의미 없음
    if length >= (end - start):
        continue
    shortcuts.append((start, end, length))

# DP 테이블
distance = [i for i in range(D + 1)]
for i in range(1, D + 1):
    distance[i] = min(distance[i - 1] + 1, distance[i])

    # i 지점으로 도착하는 지름길
    for start, end, length in shortcuts:
        if end == i:
            new_dist = distance[start] + length
            distance[i] = min(distance[i], new_dist)

print(distance[D])