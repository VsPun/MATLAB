# Physical Modeling in MATLAB by Allen B. Downey
# Chapter 2:  Scripts
# Exercise 2.1

# Computes the nth Fibonacci number.
# Precondition: you must assign a value to n before running this script. 
# Postcondition: the result is stored in ans.

from math import *

t1 = (1.0 + sqrt(5.0)) / 2.0
t2 = (1.0 - sqrt(5.0)) / 2.0
diff = t1**n - t2**n
ans = diff / sqrt(5.0)
print ">> ans = ", ans
print ""