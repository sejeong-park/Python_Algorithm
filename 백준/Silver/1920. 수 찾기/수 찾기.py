# 수찾기

n=int(input())
a=list(map(int,input().split()))
a.sort()
m=int(input())
b=list(map(int,input().split()))

def binary_search(array,target,start,end):
    while start<=end:
        mid=(start+end)//2
        if array[mid]==target:
            return 1
        elif array[mid]>target:
            end=mid-1
        else:
            start=mid+1
    return 0

for i in b:
    print(binary_search(a,i,0,n-1))
