lines_number = input() #with #
lines_number = lines_number[1:] #remove #
code_result = []

for number in range (int(lines_number)):
    code = input()

    if '#' in code:
        grate = code.index('#') #find '#' index
        code = code[:grate].rstrip() #remove everything starting with '#' and all spaces
        code_result.append(code)
    else:
        code = code.rstrip() #if no '#' in string - delete all spaces
        code_result.append(code)

print(*code_result, sep = '\n')

#alternative:
# n = input()
# for _ in range(int(n[1:])):
#     s = input()
#     if '#' in s:
#         s = s[:s.find('#')]
#     print(s.rstrip())