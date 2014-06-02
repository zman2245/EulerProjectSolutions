from PrimeNumbers import isDivisor


def getDivisors(n):
    "Returns list of divisors of the number n"
    x = 1
    results = []
    while x <= n/2:
        if isDivisor(n, x):
            results.append(x)
        x += 1

    return results

# returns list of all abundant numbers >0 and <n
def getAbundantNumbers(n):
    results = []

    x = 5
    while x <= n:
        divisors = getDivisors(x)

        # check if x is abundant by summing up its divisors
        sum = 0
        for num in divisors:
            sum += num

        if sum > x:
            print x
            results.append(x)

        x += 1

    return results
