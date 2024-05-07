palindromes = [i for i in range(100, 1001) if str(i)[0] == str(i)[-1]] #str required since indexing doesn't work with int type

print(palindromes)
