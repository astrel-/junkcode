#Project Euler
#Problem 24
#real	0m0.026s

def getListOfFact(sup):
    li = [1]
    for i in range(1,sup+1):
        li.append(li[-1]*i)
    return li

top_digit = 9
fact = getListOfFact(top_digit)
number = 10**6 - 1 # number-1
li = []
for elem in fact[::-1]:
    li.append(number/elem)
    number = number%elem
decoding = ''
digits = range(top_digit+1)
for elem in li:
    if elem:
    
        decoding += str(digits[elem])
        digits = digits[:elem]+digits[elem+1:]
    else:
        decoding += str(digits[0])
        digits = digits[1:]

print decoding


