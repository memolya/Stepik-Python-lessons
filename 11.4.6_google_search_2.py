result = []

lines_list = []
for i in range(int(input())):
    lines_list.append(input())

queries_list = []
for j in range(int(input())):
    queries_list.append(input())


for z in range(len(lines_list)): #take 1 line item per inner iteration
    counter = 0
    str_lines = str(lines_list[z])

    for q in range(len(queries_list)): #take 1 word of query per iteration
        str_queries = str(queries_list[q])

        if str_queries.casefold() in str_lines.casefold():  # if a query word appears in a line[z]: +1 to counter
            counter += 1
        else:
            break #if the query is not in the line - no point in checking other queries in this line

    if counter == len(queries_list): #if after a whole cycle of queries the counter matches the length of the query - the line is valid
        result.append(lines_list[z])

print(*result, sep='\n')




