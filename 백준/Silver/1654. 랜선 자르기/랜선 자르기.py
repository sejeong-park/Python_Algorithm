# 1654 랜선 자르기
import sys
k,n=map(int,input().split())
lan=[int(sys.stdin.readline()) for _ in range(k)]
start=1
end=max(lan) # 랜선의 최대 길이

while start<=end: #적절한 랜선의 길이를 찾는 알고리즘
    mid=(start+end)//2
    num=0 # 랜선 개수
    for i in lan: # 랜선 배열 중에서 찾기
        num+=i//mid # 분할 된 랜선 수
    if num>=n:
        start=mid+1
    else:
        end=mid-1

print(end)
