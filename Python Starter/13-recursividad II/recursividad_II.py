def my(n):
    if n > 1:
        return n * my(n-1)
    return 1
print (my(5))
