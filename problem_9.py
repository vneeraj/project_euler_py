# Script to solve Problem 9 on Project Euler
exit_flag = False
for i in range(1, 999):
    for j in range(1, 1000-i-1):
        k = 1000 - i - j
        vals = [i, j, k]
        vals.sort()        
        if (vals[2]**2 - vals[1]**2) == vals[0]**2:
            exit_flag = True
            break    
    if exit_flag:
        break
print(i, j, k, i*j*k)              