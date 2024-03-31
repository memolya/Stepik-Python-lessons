n = int(input())
text_all = []
new_text = [] # empty list to hold unique elements from the list

for i in range(n):
    text = input()
    text_all.append(text)

for j in text_all:
    if j not in new_text: # add the 1st entry to the list of unique entries
        new_text.append(j)
        
print(*new_text, sep = '\n')