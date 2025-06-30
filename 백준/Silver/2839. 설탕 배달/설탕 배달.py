N = int(input())

result = -1
for five in range(N // 5, -1, -1):
    remain = N - 5 * five
    if remain % 3 == 0:
        three = remain // 3
        result = five + three
        break

print(result)