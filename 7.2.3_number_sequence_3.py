# put your python code here
#способ с if:
# m, n = int(input()), int(input())
# for i in range(m, n-1, -1):
    # if i % 2 != 0:
        # print(i)
#способ без if:
m, n = int(input()), int(input())
start = ((m - 1) // 2) * 2 + 1
for i in range(start, n - 1, -2):
    print(i)