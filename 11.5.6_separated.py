password = input()
separator = input()

result = []
result.extend(password)

print(*result, sep = separator)

# seq = input()
# sep = input()
#
# res = sep.join(list(seq))
# print(res)