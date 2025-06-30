

N = int(input())

matrix = []
for idx in range(N):
    matrix.append(list(map(int, input().split())))

for idx in range(1, N):
    for jdx in range(len(matrix[idx])):
        # 첫번째 인덱스
        if jdx == 0:
            matrix[idx][jdx] = matrix[idx][jdx] + matrix[idx - 1][jdx]
        # 마지막 인덱스
        elif jdx == len(matrix[idx]) - 1:
            matrix[idx][jdx] = matrix[idx][jdx] + matrix[idx - 1][jdx - 1]
        else:
            matrix[idx][jdx] = matrix[idx][jdx] + max(matrix[idx - 1][jdx - 1], matrix[idx - 1][jdx])


print(max(matrix[N-1]))
