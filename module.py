def add(*n):
    return sum(n)
   
def mul(*n):
    m = 1
    for i in n:
        m *= i
    return m

def check(num):
    if num % 2 == 0 :
        return "Even"
    else:
        return "Odd"
    
def even(num):
    if num % 2 == 0 :
        return True

def odd(num):
    if num % 2 != 0:
        return True 

    