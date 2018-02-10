# Script to solve Problem 6 on Project Euler
sum_sq = 0;
sum = 0;
for i in range(100):
    sum_sq = sum_sq +  (i+1)**2
    sum = sum + (i+1)
    
diff = sum**2 - sum_sq
print(diff)   