n = input()
count = 0
for i in range(len(n)):
    if n[i].islower(): #считаем кол-во символов в нижнем регистре
        count += 1
    else: #можно не прописывать
        continue
print(count)