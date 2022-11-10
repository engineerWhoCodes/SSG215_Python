#Implementingthe relationship n(S) + n(T) = n(S U T) + n(S n T) in python
kemi = {'pounded yam', 'boli', 'rice', 'dodo', 'yams', 'eggs', 'beans', 'water melon', 'mango', 'egusi', 'bananas', 'pine apples', 'apples', 'eggs', 'oranges'}

imman = {'moin-moin', 'eko', 'boli', 'jollof-rice', 'amala', 'eggs'}
kemiNum = len(kemi)
immanNum = len(imman)
unionNum = len(kemi.union(imman))
intNum = len(kemi.intersection(imman))
if(kemiNum + immanNum == unionNum + intNum):
    print('The formula is correct')
else:
    print('It is wrong')