# put your python code here
counter_coin = 0
num = int(input())
while num != 0:
    while num >= 25:
        counter_coin += 1
        num -= 25
    while num >= 10 and num <= 25:
        counter_coin += 1
        num -= 10
    while num >= 5 and num <= 10:
        counter_coin += 1
        num -= 5
    while num >= 1 and num <= 5:
        counter_coin += 1
        num -= 1
print(counter_coin)