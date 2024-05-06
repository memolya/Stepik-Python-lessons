text = input().split()

count_artciles_a = text.count('a')
count_artciles_an = text.count('an')
count_artciles_the = text.count('the')
count_artciles_a_capitalized = text.count('A')
count_artciles_an_capitalized = text.count('An')
count_artciles_the_capitalized = text.count('The')

print('Общее количество артиклей:', count_artciles_a + count_artciles_an + count_artciles_the + count_artciles_a_capitalized + count_artciles_an_capitalized + count_artciles_the_capitalized)
