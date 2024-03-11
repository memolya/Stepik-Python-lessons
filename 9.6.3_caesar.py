shift = int(input())
text = input()

for i in range(len(text)):
    #print('old_symb_id =', ord(text[i]), 'old_symb =', chr(ord(text[i]))) - debug
    new_ord = ord(text[i]) - shift #shift according to the input
    #print('new_ord=', new_ord) - debug
    if new_ord >= 97: #IDs can only start from 97 (symb. 'a')
        print(chr(new_ord), end = '')
        #print('new_symb =', chr(new_ord))  # , end = '') - debug
    else:
        new_ord += 26
        print(chr(new_ord), end = '')
        #print('new_symb =', chr(new_ord)) - debug



