# Simple tokenization With list comprehension
'''
def sep(word):
    return [char for char in word]
sentOne = 'the quick brown fox jumps over the lazy dog'
listOne = sentOne.split() #splitting sentOne which returns a list
firstList = sep(listOne[0]) #returning the result of listOne as single characters in a list
firstSet = set(firstList) #turning the result of firstList into a set
for word in listOne[1:]:
    firstSet = set(sep(word)).union(firstSet)
print(len(firstSet))

#Without list comprehension(this is more verbose than the former lines of code)
def sep(word):
    list1 = []
    for x in word:
        list1.append(x)
    return list1
sentOne = 'the quick brown fox jumps over the lazy dog'
listSent = sentOne.split()

#The below codes performes same function
list2 = []
for wrd in listSent:
    list2 += sep(wrd)
'''

