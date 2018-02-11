# Script to solve Problem 7 on Project Euler
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

cur_val = 2
prime_count = 0
last_prime = 0
target = 10001

while prime_count < target:
    if primality_test(cur_val):
        prime_count += 1  
        last_prime = cur_val
        
    cur_val += 1
    
print(last_prime)