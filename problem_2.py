# Script to solve Problem 2 on Project Euler
sum = 0
prev_val = 1
cur_val = 1

while cur_val < 4E6:
    new_val = cur_val + prev_val
    prev_val = cur_val
    cur_val = new_val
	
    if (cur_val % 2) == 0:
	    sum = sum + cur_val
	
print(sum)