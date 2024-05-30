# put your python code here

n = int(input())
max1 = 0
max2 = 1
for i in range(1, n+1):
    num = int(input())
    if num > max1:
        max2 = max1 #в переменную max2 кладём max1
        max1 = num  #в переменную max1 кладём аргумент; в следующих итерациях num сравниваем сначала с max1 - если он больше, то бывший max1 переезжает в max2, если нет - сравниваем num c max2 - если он больше старого max2, кладём туда. Если нет, то откидываем.
    elif num > max2:
        max2 = num
print(max1, max2, sep = '\n')