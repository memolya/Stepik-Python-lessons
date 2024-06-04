# Splitting on UpperCase using re
import re

def convert_to_python_case(text):

    res_list = []
    res_list = re.findall('[A-Z][^A-Z]*', txt)
    lowercase_list = [s.lower() for s in res_list]
    print(*lowercase_list, sep = '_')

# считываем данные
txt = input()

# вызываем функцию
# print(convert_to_python_case(txt))
(convert_to_python_case(txt)) #don't use 'print' before function call to avoid returning 'none'