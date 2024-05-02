numbers_list = input().split()
result = list(map(int, numbers_list)) #we make a list of digits (from numbers_list) turned into int by map function
min, max = result.index(min(result)), result.index(max(result))
result[min], result[max] = result[max], result[min]
print(*result)