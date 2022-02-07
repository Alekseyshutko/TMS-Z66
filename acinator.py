# acinator
# карлосон
# чебурашка
# малыш
# гена
print('Make a wish for one of the characters: Carloson, Cheburashka, Malysh, Gena')
print('answer Yes or No')
k = input('Is it a person?  ').lower()
if k == 'yes':
    k1 = input("Does he wear clothes?  ").lower()
    if k1 == 'yes':
        k2 = input('Can he fly?  ').lower()
        if k2 == 'yes':
            print('This is Carloson  ')
        else:
            print('Malysh')
    else:
        k2 = input('Can he fly?  ').lower()
        if k2 == 'yes':
            print('This is Carloson')
        else:
            print('Malysh')

else:
    k3 = input('does he have ears?  ').lower()
    if k3 == 'Yes':
        k4 = input('is it green?  ').lower()
        if k4 == 'Yes':
            print('Gena')
        else:
            print('Cheburashka')
    else:
        k4 = input('is it green?  ').lower()
        if k4 == 'Yes':
            print('Gena')
        else:
            print('Cheburashka')
