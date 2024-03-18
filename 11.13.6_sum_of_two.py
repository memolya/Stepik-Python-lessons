n = int(input())
numbers =[]
final = []
short_list = []

for i in range(n):
    # input all the numbers
    inserted_number = int(input())
    # make a list of all the numbers
    numbers.append(inserted_number)
#print(numbers) #get a list of all the numbers without sums - debug

#use -1 in range so the last number sums with the one to the left only
for i in range (len(numbers)-1):
    # indexes 0 and 1 transfer into a short list
    short_list = numbers[0:2]
    #print('short_list =', short_list) #see numbers for each iteration - debug
    sum_of_2 = sum(short_list)
    #print(sum_of_2) #a sum of each 2 items - debug
    final.append(sum_of_2)
    #delete item with index 0 so we shift to the right once
    del numbers[0]
print(final)


