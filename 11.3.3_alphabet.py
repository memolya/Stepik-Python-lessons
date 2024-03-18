alphabet = 'abcdefghijklmnopqrstuvwxyz'
chars = list(alphabet) #convert the alphabet into a list []
all_letters = []
for i in range(26):
    letter = [chars[i]*(i+1)]
    all_letters += letter
print(all_letters)
