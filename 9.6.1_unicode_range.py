chr1, chr2 = chr(int(input())), chr(int(input()))
for i in range(ord(chr1), ord(chr2)+1): #can only put 1 argument into ord, so we type ord 2 times
    print(chr(i), end = ' ')