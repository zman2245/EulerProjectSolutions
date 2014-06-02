from PrimeNumbers import isPrime

def quad(x, a, b):
    res = x*x
    res = res + x*a + b
    return res


a = -1000
numPrimes = 0
currentMaxProd = 0
currentMaxPrimes = 0

while a <= 1000:
    b = -1000
    while b <= 1000:
        n = 0

        while n < 100:
            x = quad(n, a, b)

            if x > 0 and isPrime(x):
                numPrimes += 1
            else:
                numPrimes = 0
                n = 100

            if currentMaxPrimes < numPrimes:
                currentMaxPrimes = numPrimes
                currentMaxProd = a * b


            n += 1
        b += 1
    a += 1

print currentMaxProd
