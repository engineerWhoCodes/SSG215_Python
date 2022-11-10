#Checking if the list of what I am wearing is a subset of Ade's or a disjoint set with Ade's.

ade = {'singlet', 'shorts', 'teeshirt', 'slippes', 'headphones', 'wristwatch', 'boxers',}
imman = {'longsleeve', 'trousers', 'slippers, boxers'}
if ade.intersection(imman) == imman:
    print('What Imman is wearing is a subset of Ade\'s')
elif len(ade.intersection(imman)) == 0:
    print('The two have nothing in common')
else:
    print('There are some things unique to both')