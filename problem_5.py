# Script to solve Problem 5 on Project Euler
from fractions import gcd

def lcm(x, y):
    return int((x*y)/gcd(x, y))

lcm_val = 1
for i in range(1, 20):
    lcm_val = lcm(i, lcm_val)

print(lcm_val)    