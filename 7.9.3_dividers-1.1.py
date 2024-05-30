num_1, num_2 = int(input()), int(input())
temporary_dividers_sum = 0
temporary_largest = 0
largest = 0
for num in range(num_1, num_2 + 1): #ищем число с максимальной суммой делителей, тут числовой отрезок
    for i in range(1, num+1): #делим каждое число с шагом 1, начиная с 1
        if num % i == 0:
            temporary_dividers_sum += i #сумматор для делителей
            if temporary_dividers_sum >= temporary_largest:
                temporary_largest = temporary_dividers_sum
                largest = num
    temporary_dividers_sum = 0
print(largest, temporary_largest, end = ' ')
