n = int(input())
counter_of_3 = 0 #количество цифр 3 в нем;
last_num_memory = n % 10
counter_of_last_num = 0 #сколько раз в нем встречается последняя цифра;
counter_of_evens = 0 #количество четных цифр;
sum_of_morefives = 0 #сумму его цифр, больших пяти;
multiplication_of_moresevens = 1 #произведение цифр, больших семи (если цифр больших семи нет, то вывести 1, если такая цифра одна, то вывести ее);
counter_of_zerofives = 0 #сколько раз в нем встречается цифры 0 и 5 (всего суммарно).

while n > 0:
    last_num_fact = n % 10 #сюда складывается последняя цифра
    if last_num_fact == 3: #кол-во троек
        counter_of_3 += 1
    if last_num_fact == last_num_memory: #считаем кол-во повторений последней цифры
        counter_of_last_num += 1
    if last_num_fact % 2 == 0: #считаем четные цифры
        counter_of_evens += 1
    if last_num_fact > 5: #сумма цифр, больших 5
        sum_of_morefives += last_num_fact
    if last_num_fact > 7: #произведение цифр, больших 7
        multiplication_of_moresevens *= last_num_fact
    if last_num_fact == 0 or last_num_fact == 5: #кол-во 0 и 5
        counter_of_zerofives += 1

    n //= 10
print(counter_of_3, counter_of_last_num, counter_of_evens, sum_of_morefives, multiplication_of_moresevens, counter_of_zerofives, sep='\n')