#Project Euler
#Problem 21
#real	0m0.128s

from math import sqrt

def sumOfDivisors(number):
    """
    returns sum of divisors of n
    """
    if not number-1: return 1
    result = 1
    if int(sqrt(number)) == sqrt(number):
        result += int(sqrt(number))
        n = int(sqrt(number))
    else:
        n = int(sqrt(number))+1
    for i in range(2,n):
        if not number%i:
            result += i+number/i
    return result

sum = 0
for i in range(2,10001):
    a = sumOfDivisors(i)
    sum +=  a-i > 0 and \
            sumOfDivisors(a) == i and \
            i+a or 0
print sum