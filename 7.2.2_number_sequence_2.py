# put your python code here
m, n = int(input()), int(input())
for i in range(m, n + 1):
    if m < n:
        print(i)
else:
    for i in range(m, n - 1, -1):
        print(i)