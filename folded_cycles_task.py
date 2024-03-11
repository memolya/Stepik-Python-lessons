for n in range (1, 29):
    for k in range(1, 31):
        for m in range(1, 32):
            if 28 * n + 30 * k + 31 * m == 365:
                print('n = ', n, 'k = ', k, 'm = ', m)
print()