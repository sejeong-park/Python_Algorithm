from math import comb
T = int(input())

for _ in range(T):
    N, M = map(int, input().split())
    combs = comb(M, N)
    print(combs)