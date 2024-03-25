#amount of strings
num_lists = int(input())
#empty list for the result
result = []
lists = []
temp = 0

#user enters the strings -> we create a list - 1 entry - 1 element
for i in range(num_lists):
    user_input = (input())
    lists.append(user_input)

# user inputs the order of the searched letter
k = int(input())
# print(lists) - debug

#check 1 element of the list per iteration
for j in range(len(lists)):
    #check 1 symbol of the element
    temp = lists[j]
    #if the element is too short and doesn't contain the symbol #k - we go on
    # if the element contains #k symbol (-1 since start from 0) we add it up to the final list
    if len(temp) > k-1:
        result.append(temp[k-1])
        #print(result) - debug

# using list comprehension
print(''.join(result))