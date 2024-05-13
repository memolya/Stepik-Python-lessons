L, M = input().split(), input().split()
result = []

for i in range(len(L)):
    result.append(int(L[i]) + int(M[i]))
print(*result)