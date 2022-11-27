
#Finding unions and intersections of intervals.
import portion as por
porSet_01 = por.closed(0, 20)
porSet_02 = por.openclosed(4, 27)
porSet_03 = por.closed(13, 35)
uniInt = porSet_01.union(porSet_02)
intSet = porSet_03.intersection(porSet_01)

pass
