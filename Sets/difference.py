#Justifying that n(A-B) + n(B-A) = n(AuB) - n(AnB) and
# n(A) +n(B) = n(AuB) + n(AnB)
#A.difference(B) evaluates to B-A
olu = {'eba', 'okro', 'yam', 'beans', 'boli', 'rice', 'stew',}
chike = {'rice', 'ugwu', 'akpu', 'beans', 'plaintains', 'yam', 'agazi'}
diffOne = chike.difference(olu) #The elements in chike not in olu
diffTwo = olu.difference(chike) #The elements in olu butnot in chike
intOne = chike.intersection(olu)
intTwo = olu.intersection(chike)
uniOne = chike.union(olu)
uniTwo = olu.union(chike)
#testOne = (len(diffOne) + len(diffTwo)) == (len(uniOne) - len(intOne))
#testTwo = (len(olu) + len(chike)) == (len(intOne) + len(uniOne))
pass
#Another way to write the 12th and 13th code will be
a = len(diffOne) + len(diffTwo)
b = len(uniOne) - len(intOne)
testOne = a == b
print(testOne)