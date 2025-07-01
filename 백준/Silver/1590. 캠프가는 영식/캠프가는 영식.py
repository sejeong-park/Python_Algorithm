"""
1590_캠프가는 영식
"""
N, T = map(int, input().split())
result = []
for _ in range(N):
    S, I, C = map(int, input().split())
    time = [S + (I * t) for t in range(C)]
    if time[-1] < T:
        continue
    start = 0
    end = C - 1

    while start <= end:
        mid = (start + end) // 2
        if time[mid] >= T:
            answer = mid
            end = mid - 1
        else:
            start = mid + 1

    result.append(time[answer] - T)

if result:
    print(min(result))
else:
    print(-1)
