"""
수빈 N & 동생 J
수빈 : 걷거나 순간이동 가능
- 걷기 : 수빈위치가 X일 때 걸으면 1초 후 X - 1, X + 1로 이동
- 순간이동 : 1초 후 2*X로 이동
결과 : 동생을 찾을 수 있는 가장 빠른 시간 몇 초 후?
-> 전략: 백트래킹
"""
from collections import deque

N, K = map(int, input().split())
MAX = 100000
distance = [0] * (MAX + 1)

def bfs(start):
    queue = deque([start])
    while queue:
        x = queue.popleft() # current index
        if x == K:
            return distance[x]
        for nx in (x+1, x-1, x*2):
            if 0 <= nx <= MAX and not distance[nx]:
                distance[nx] = distance[x] + 1
                queue.append(nx)

result = bfs(N)
print(result)