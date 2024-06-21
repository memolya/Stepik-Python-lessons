def convert():
    # print(bin(num))
    # print(oct(num))
    # print(hex(num))

    #binary
    print(format(num, 'b'))
    #octal
    print(format(num, 'o'))
    #hexadecimal
    print(format(num, 'X'))

num = int(input())
convert()