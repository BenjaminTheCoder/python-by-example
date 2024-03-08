from operator import add, mul
from functools import reduce


mult_anwser = reduce(add, [3,3,3], 0)
print(mult_anwser)
power_anwser = reduce(mul, [3]*3, 1)
print(power_anwser)
















    
