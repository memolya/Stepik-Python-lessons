for n in range(1, 11):
    for m in range(1, 21):
        for l in range(1, 101):
            if 10 * n + 5 * m + 0.5 * l == 100 and n + m + l == 100:
                print('n = ', n, 'm = ', m, 'l = ', l)
print()