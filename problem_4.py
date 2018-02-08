# Script to solve Problem 4 on Project Euler
max_palindrome = 0;

for i in range(100, 999):
    for j in range(100, 999):
        product = i*j
        if (str(product) == str(product)[::-1]) and product > max_palindrome:
            max_palindrome = product
            
print(max_palindrome)      
print(i, j)