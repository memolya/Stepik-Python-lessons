n = int(input())
counter = 0
for i in range(n):
    messages = input()
    if messages.count('11') >= 3:
        counter += 1
print(counter)