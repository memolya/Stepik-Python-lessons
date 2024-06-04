# логарифм X по основанию 2 (на каждой итерации мы отбрасываем половину чисел и гарантировано угадаем задуманное число за величину, равную log2n (двоичный логарифм) округленную до целого в большую сторону)
from math import log2 as l
# округление в большую сторону math.ceil(x) -> int / float  x : Число, которое требуется округлить. Возвращает наименьшее целое (до 3.0 в виде числа с плавающей запятой), большее, либо равное x
from math import ceil as c


def count_moves(n):
    return c(l(n))

print(count_moves(int(input())))

# n = int(input())
# attempts = 0
#
# while 2 ** attempts < n:
#     attempts += 1
#
# print(attempts)