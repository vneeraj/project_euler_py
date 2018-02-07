# Script to solve Problem 3 on Project Euler
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
        for i in range(7, max_candidate):
            if (x % i == 0):
                return False
        return True

input_val = 600851475143

# Loop over possible factors up to sqrt(input)
for i in range(2, math.ceil(math.sqrt(input_val))):
    if (input_val % i == 0) and primality_test(i):
        # Since we only go up to sqrt(input), we have to check codivisor as well
        # If codivisor here is also prime, it is guaranteed to be the largest
        if(primality_test(input_val/i)):
            max_prime_factor = input_val/i
            break
        else:
            max_prime_factor = i         
        
print(max_prime_factor)
print(primality_test(max_prime_factor))