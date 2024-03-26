n = int(input())
user_entered = []

for i in range(n):
    user_input = int(input())
    user_entered.append(user_input)
    print(user_input)

print()

for z in range(len(user_entered)):
    print(user_entered[z]**2 + 2*user_entered[z] +1)