n = int(input())
for i in range(1, n+1): #столбики по вертикали до n
    print(i, end='') #end = '', чтобы плюсы выводились не с новой строки, а сразу следом за i
    for j in range(1, i+1): #горизонтальная печать "+"
        if i % j == 0:
            print('+', end = '')
    print() #print в теле вложенного цикла, чтобы перенос строки происходил после вывода всех "+" на строке - перекидывает на следующую итерацию i
