n = int(input())
all_texts = []
result = []

for i in range(n):
    phrases = input()
    all_texts.append(phrases)

search_query = input()

for j in all_texts:
    if search_query.casefold() in j.casefold(): #casefolding the query and an element of the list to avoid case sensitivity
        result.append(j)

print(*result, sep = '\n')

