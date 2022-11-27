#Justify n(S) +n(T) = n(SuT) + n(SnT)
a = {1, 2, 3, 4, 5}
b = {2, 7, 1, 8, 5}
aNum = len(a)
bNum = len(b)
intSet = a.intersection(b)
uniSet = a.union(b)
intSetNum = len(intSet)
uniSetNum = len(uniSet)
if aNum + bNum == intSetNum + uniSetNum:
    print('The formular is justified')
else:
    print('Not valid')