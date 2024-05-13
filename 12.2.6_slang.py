# text = input().split()
# for c in text:
#     print(c[1:], c[0], 'ки', sep = '', end = ' ')

words = [word[1:] + word[0] + "ки" for word in input().split()]

print(*words)