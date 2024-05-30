n = int(input())
sum_1 = 0
sum_2 = 0
while n % 10 > 0:
    sum_1 += n % 10
    n //= 10
while sum_1 % 10 > 0:
    step = sum_1 % 10
    sum_1 //= 10
    sum_2 += step
print(sum_2)

###
n = int(input())
sum_1 = 0
sum_2 = 0
while n > 0:
    sum_1 += n % 10
    n //= 10
while sum_1 > 10:
    step = sum_1 % 10
    sum_1 //= 10
    sum_2 += step
print(sum_2)

###
#этот код правильный, потому что на последнем цикле складываются числа, которые требуют сложения трехзначного
n = int(input())
sum_1 = 0
sum_2 = 0
sum_3 = 0
while n > 0:
    sum_1 += n % 10
    n //= 10
while sum_1 > 0:
    step = sum_1 % 10
    sum_1 //= 10 #эту и следующую строку можно для красоты поменять местами, чтобы было единообразно с соседними циклами
    sum_2 += step
while sum_2 > 0:
    sum_3 += sum_2 % 10
    sum_2 //= 10
print(sum_3)
