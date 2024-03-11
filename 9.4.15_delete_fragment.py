new_n = 0
n = input()
left, right = (n.index('h')), (n.rindex('h'))
if left and right:
    new_n = n[:left] + n[right+1:]
    print(new_n)
else:
    print('')