
X, Y = map(int, input().split())
Z = (Y * 100) // X
start = 1
end = 1000000000
result = 0
while start <= end:
    mid = (start + end) // 2 # 이분 탐색
    # 조건
    if (Y + mid)*100 // (X + mid) > Z:
        end = mid - 1
        result = mid

    else:
        start = mid + 1

print(result if result !=0 else -1 )