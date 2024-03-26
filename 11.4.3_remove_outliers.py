n = int(input())
all_data = []

for i in range(n):
    user_input = int(input())
    all_data.append(user_input)

all_data.remove(min(all_data))
all_data.remove(max(all_data))

print(*all_data, sep = '\n')