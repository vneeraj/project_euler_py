#Script to solve Problem 15 on Project Euler
def factorial(n):
    if not isinstance(n, int):
        raise TypeError('Input must be integer!')
    if n < 0:
        raise ValueError('Input must be nonnegative!')
            
    if n == 1 or n == 0:
        return 1
    else:
        return n*factorial(n-1)
        
def nchoosek(n, k):
    if (not isinstance(n, int)) or (not isinstance(k, int)):
        raise TypeError('Inputs must be  integers!')
    if n < 0 or k < 0:
        raise ValueError('Inputs must be nonnegative!')        
    if k > n:
        raise ValueError('k must be <= n!')        
    
    if k == n:
        return 1
    else:
        return int((n * nchoosek(n-1, k))/(n - k))

print(nchoosek(40, 20))