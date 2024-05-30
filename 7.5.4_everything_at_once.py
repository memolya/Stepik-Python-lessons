# put your python code here
num = int(input())
sum = 0
counter = 0
multiplyer = 1
totally_last_digit = num % 10 #считать до цикла, тк в теле цикла num будет делиться на 10 без остатка, пока не будет равен 0
while num != 0:
    last_digit = num % 10
    sum += last_digit
    multiplyer *= last_digit
    num = num // 10
    counter += 1
average = sum / counter
print(sum) #сумма всех цифр
print(counter) #количество цифр
print(multiplyer) #произведение цифр
print(average) #среднее арифметическое
print(last_digit) #первая цифра, тк после прокрутки цикла в last_digit осталась первая цифра
print(last_digit + totally_last_digit) #сумма первой и последней цифры