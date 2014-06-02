# The number 3797 has an interesting property. Being prime itself, it is possible to continuously remove digits from left to right, and remain prime at each stage: 3797, 797, 97, and 7. Similarly we can work from right to left: 3797, 379, 37, and 3.
# 
# Find the sum of the only eleven primes that are both truncatable from left to right and right to left.
# 
# NOTE: 2, 3, 5, and 7 are not considered to be truncatable primes.

from PrimeNumbers import *

def truncLeft(x):
    xs = str(x)
    return xs[1:]

def truncRight(x):
    xs = str(x)
    return xs[:-1]

i           = 10
results     = []
primes      = [2, 3, 5, 7]

# it's given that there are only 11
while len(results) < 11:
    i += 1
    if isPrime(i):
        primes.append(i)

        istr = str(i)
        lstr = truncLeft(istr)
        rstr = truncRight(istr)

        while len(lstr) > 0:
            if int(lstr) not in primes:
                break

            if int(rstr) not in primes:
                break

            lstr = truncLeft(lstr)
            rstr = truncRight(rstr)

        if len(lstr) == 0:
            print i
            results.append(i)

print sum(results)

