'''
If P = {x:1<=x<=6}, and Q = {x:2<x<9} x E ,
find P n Q
'''
import portion as por
intP = por.closed(1, 6)
intQ = por.open(2, 9)
comprP = {values for values in range(2, 7)}
comprQ = {values for values in range(3, 9)}
intPor = intP.intersection(intQ)
intComp = comprP.intersection(comprQ)
print(intPor)