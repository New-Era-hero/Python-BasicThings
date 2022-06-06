from math import factorial

def my_factorial(n):
    factorial_total = 1
    while n > 1:
        factorial_total *= n
        n -= 1
    return factorial_total

print (factorial(5))
print (my_factorial(6))

print (6 * 5 * 4 * 3 * 2 * 1)
        
