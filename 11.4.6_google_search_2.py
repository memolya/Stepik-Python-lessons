import deepdiff

#number of lines
n = int(input())
all_texts = []
all_queries = []
result = []

for i in range(n):
    phrases = input()
    all_texts.append(phrases)

#number of search queries
k = int(input())
for z in range(k):
   search_query = input()
   all_queries.append(z)

#for j in all_texts:
deepdiff.DeepDiff(search_query, all_texts, ignore_string_case=True)
    #if search_query.casefold() in j.casefold(): #casefolding the query and an element of the list to avoid case sensitivity
        result.append(j)

print(*result, sep = '\n')