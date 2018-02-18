#Script to solve Problem 14 on Project Euler
collatz_history = {}
def collatz_count(x):
    if x in collatz_history:
        return collatz_history[x]
    else:   
        if x == 1:            
            y = 0
        elif x % 2 == 0:
            y = x/2
        else:
            y = 3*x + 1
        
        if y == 0:
            collatz_history[x] = 1
        elif y == 1:
            collatz_history[x] = 2
        else:
            collatz_history[x] = 1 + collatz_count(y)
    return collatz_history[x]
   
max_len = 0
max_len_source = 0
for i in range(int(1E6)):
    cur_count = collatz_count(i)
    if(cur_count > max_len):
        max_len = cur_count
        max_len_source = i
        
print(max_len_source, max_len)      