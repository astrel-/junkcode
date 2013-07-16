#Project Euler
#Problem 16
#real	0m0.079s

def doubleNumber(li):
    """
    li is reversed list of digits in number
    returns reversed list of digits in 2*number
    """
    digit = 0
    for idx, val in enumerate(li):
        if 2*val+digit>9:
            li[idx] = 2*val-10+digit
            digit = 1
        else:
            li[idx] = 2*val+digit
            digit = 0
    if digit: li.append(digit)
    return li
            
li = [1]
n = 1000
for i in range(n):
    li = doubleNumber(li)
print sum(li)
    