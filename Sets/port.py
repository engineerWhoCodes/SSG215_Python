#The portion module provides data struture and operations for intervals in python
import portion as por
from matplotlib_venn import venn2, venn2_circles
import matplotlib.pyplot as plt
compSet_1 = {i for i in range(0, 21)} #list comprehension
compSet_2 = {iota for iota in range(15, 27)} #list comprehension
porSet_1 = por.closed(0, 20)
porSet_2 = por.openclosed(4, 27)
porSet_3 = por.closed(13, 35)
answer = 3.5 in porSet_2
test = 18 in compSet_2.intersection(compSet_1)
venn2([compSet_1, compSet_2],
set_labels = ('First set', 'Second set'),
set_colors = ('purple', 'yellow'), alpha = 0.8)
venn2_circles([compSet_1, compSet_2])
#plt.title('Sample code')
#plt.show()
#The above lines of codes is to prove that sets can involve discrete elements, comprehensions as well intervals.
print(test)