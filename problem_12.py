# Script to solve Problem 7 on Project Euler
import math

# Returns number of divisors of input number
def count_div(x):
    num_divisors = 2; # 1 and itself always
    
    # Loop over potential factors between 2 and sqrt(x)
    max_candidate = int(math.floor(math.sqrt(x)))
    for i in range(2, max_candidate+1):
        if (x % i == 0):
            if (i*i == x):
                num_divisors += 1 # perfect square                
            else:
                num_divisors += 2                
    return num_divisors
    
cur_num = 0
cur_num_div = 0
count = 1
while (cur_num_div < 500):
    cur_num += count
    count += 1
    cur_num_div = count_div(cur_num)
    
print(cur_num)    