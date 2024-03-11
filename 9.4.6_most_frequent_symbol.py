n = input()
n = n[::-1]
print(max(n, key = n.count))