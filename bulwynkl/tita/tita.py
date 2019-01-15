#!/usr/bin/env python3

'''

author bulwynkl
initialised 2019-01-15
'''

import os
import numpy as np

'''
intent...

display a multiplication sum and wait for an answer
compare to expected value (numbers only)#!/usr/bin/env python3
record correct or wrong
display heat map every 10 attempts
ignore 1 x table
up to 12 times initially

2x2 -> 12x12


array of values:
2 ->12
2->12
count of True
count of False

levels - expand range, introduce time limits to force guessing

'''

print("Welcome to the times tables tutor")
print()


a=[i+2 for i in range(11)]
b = [i+2 for i in range(11)]
print(a)
print(b)
results = np.zeros(shape=(11,11,2), dtype=int)
#print(results)

print("     2   3   4   5   6   7   8   9   10   11   12  ")

for i in range(11):
    thisline =  str(i+2) + "   "
    for j in range(11):
        thisline=thisline+str(results[i][j][0])+"/"+str(results[i][j][1])+"  "
    print(thisline)
