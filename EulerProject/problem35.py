# The number, 197, is called a circular prime because all rotations of the digits: 197, 971, and 719, are themselves prime.
# 
# There are thirteen such primes below 100: 2, 3, 5, 7, 11, 13, 17, 31, 37, 71, 73, 79, and 97.
# 
# How many circular primes are there below one million?

from PrimeNumbers import *

def rotateNum(x):
   xs = str(x)
   xs = xs[-1] + xs[:-1]
   return int(xs)

primes      = []
circ_primes = []

for i in range(1,1000000):
    cur     = i
    isValid = True
    for j in range(0, len(str(i))):
        if cur < i and cur not in circ_primes:
            isValid = False
            break
        elif not isPrime(cur):
            isValid = False
            break
       
        cur = rotateNum(cur)

    if isValid == True:
        circ_primes.append(i)

print circ_primes
print len(circ_primes)
