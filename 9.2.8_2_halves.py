text = input()
first_part, second_part = text[:len(text)//2], text[len(text)//2:] #The mid index can be calculated as len(text)//2. Once you have the mid index, the first half can be extracted by slicing the string from the start till the mid index. While the Second half can be extracted by slicing the string from the mid index till the end.
if len(first_part) == len(second_part): #если длины строк равны
    print(second_part, first_part, sep ='')
else:
    first_part = text[:len(text) // 2 + 1] #делим строку до середины, +1, чтобы прибавить оставшуюся лишней букву к первой части
    second_part = text[int(len(first_part)):] #'первая буква' = [длина первой строки], т.к. у первой буквы индекс 0, и в первой части на 1 меньше индекс, чем кол-во символов , преобр в int
    print(second_part, first_part, sep ='')