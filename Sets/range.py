#Testing range and list comprehension
a1 = range(-10, 10, 2)
b1 = [i for i in a1]
a2 = range(8, -12, -2)
b2 = [j for j in a2]
s1 = set(b1)
s2 = set(b2)
listSquares = []
if b1 == b2:
    print('The list are the same')
else:
    print('Different lists')
if s1 == s2:
    print('The sets are the same')
else:
    print('Different sets')
for k in b1:
    listSquares.append(k * k)
otherList = [l * l for l in  a1]
#The sets are the same because they contain the same equal elements.
#The lists are not the same because the order of lists b1 and b2 are not the same even though they conatain equal length of elements.
print(otherList)

