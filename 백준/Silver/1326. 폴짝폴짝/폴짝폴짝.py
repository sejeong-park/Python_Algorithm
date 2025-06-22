"""
1326_폴짝폴짝
- 일렬의 징검다리 -> 폴짝 뛰댕김
- 징검다리에서 점프할 때 그 징검다리에 쓰여 있는 수의 배수만큼 떨어져 있는 곳으로 갈 수 있음
- a -> b 최소 몇 번 점프해서 b에 도착 가능?
"""

from collections import deque

N = int(input())
bridge = list(map(int, input().split()))
a, b = map(int, input().split())
visited = [False] * (N + 1)

def bfs(start, end):
    visited[start] = True
    queue = deque([(start, 0)])

    while queue:
        current, jump = queue.popleft()
        # 만약 현재 위치가 end와 일치하다면
        if current == end:
            return jump

        num = bridge[current - 1] # 징검다리에 적힌 숫자

        # 이동 방향은 앞과 뒤
        for direction in [-1, 1]:
            mul = 1 # 배수 곱
            while True:
                next = current + num * direction * mul
                # 이동 거리 밖으로 나가면 이동 종료
                if next < 1 or next > N:
                    break
                if not visited[next]:
                    visited[next] = True
                    queue.append((next, jump + 1))
                mul += 1

    return -1

result = bfs(a, b)
print(result)
