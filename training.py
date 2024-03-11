num = int(input())
last_number = num % 10
print(last_number)
before_last_number = (num % 100) // 10
print(before_last_number)
before_before_last_number = (num // 100) % 10
print(before_before_last_number)
first_number = num // 1000
print(first_number)
