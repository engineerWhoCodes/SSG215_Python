#Testing operators and precedence
'''
t1 = 3 / 4 * 2
t2 = 3 / (4 * 2)
print(t1)
print(t2)

meal = 'Bread'
money = 0
if meal == 'Bread' or meal == 'Fruit' and money >= 2:
    print('Lunch is being delivered')
else:
    print('Can\'t deliver lunch')
#The above code runs(not the desired output) even when money is 0. But this cabb be corrected using an operator of higher precedence to give us desired output.
if (meal == 'Bread' or meal == 'Fruit') and money >= 2:
    print('Lunch is being delivered')
else:
    print('Can\'t deliver lunch')
'''
#Testing for associativity for operators with the same level of precedence.
#Left to right associativity
print(5 * 2 // 3)
#Left to right associativity
print(5 * (2 // 3))