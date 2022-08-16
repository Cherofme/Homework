# from math_func import (square and rectangle)
from math_func import square as sq
from math_func import rectangle as rec

#Then assign square 1-st and 2-nd
s_1 = sq(10)
s_2 = rec(4, 5)
# Just sub 2 result
result = s_1 - s_2
print(result)

if result > 0:
    print('s1 > s2')
elif result < 0:
    print('s1 < s2')
else:
    print('s1 = s2')