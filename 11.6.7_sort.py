symbols = input().split()
result = list(map(int, symbols))
result.sort()
print(*result)
result.sort(reverse=True)
print(*result)