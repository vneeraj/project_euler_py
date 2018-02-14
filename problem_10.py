# Script to solve Problem 10 on Project Euler
import math

# Returns true if x is prime
def primality_test(x):
    if x == 0 or x == 1:
        return False
    # Quick checks of 2, 3, 5
    elif x == 2 or x == 3 or x == 5:
        return True
    elif (x % 2 == 0) or (x % 3 == 0) or (x % 5 == 0):
        return False
    else:
        # Loop over potential factors between 7 and sqrt(x)
        max_candidate = int(math.ceil(math.sqrt(x)))
        for i in range(7, max_candidate+1):
            if (x % i == 0):
                return False
        return True
        
sum = 0
val = 2
while val < 2E6:
    if primality_test(val):
        sum = sum + val
    val += 1
    
print(sum)    