text = input()
print(text[2]) #третий символ строки
print(text[-2]) #предпоследний символ из строки
print(text[:5]) #первые 5 символов
print(text[:-2]) #вся строка, кроме последних 2 символов
print(text[0::2])  # even  - start at the beginning at take every second item + excluding the first element #все символы с четными индексами
print(text[1::2]) #If we omitted start, the default (0) would be used. So the first element (at position 0, because the indexes are 0-based) would be selected. In this case the second element will be selected. #We also provided third argument (step) which is 2. Which means that one element will be selected, the next will be skipped, and so on...
print(text[::-1]) #в обратном порядке
print(text[::-2]) #в обратном порядке через 1 начиная с последнего