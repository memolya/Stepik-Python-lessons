n = int(input())

for j in range(1, n+1):
    lines = input()
    if len(lines) == 0:
        lines += ' '
    if lines.isspace() == False:
        print(j, ':', ' ', sep = '', end = '')
        print(lines)
    else:
        print(j, ':', ' ', sep = '', end = '')
        print('COMMENT SHOULD BE DELETED')
