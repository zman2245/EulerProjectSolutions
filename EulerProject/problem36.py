# The decimal number, 585 = 10010010012 (binary), is palindromic in both bases.
# 
# Find the sum of all numbers, less than one million, which are palindromic in base 10 and base 2.
# 
# (Please note that the palindromic number, in either base, may not include leading zeros.)

def isPalindrome(s):
    low     = 0
    high    = len(s) - 1
    while low < high:
        if s[low] != s[high]:
            return False
        low += 1
        high -= 1

    return True

def getBase2Str(x):
    val = 1
    while val <= x:
        val *= 2

    binRep = ""
    valRemaining = x

    while val > 1:
        val /= 2

        if val <= valRemaining:
            valRemaining -= val
            binRep += "1"
        else:
            binRep += "0"

    return binRep

palindromes = []
for i in range(1,1000000):
    if isPalindrome(str(i)):
        binRep = getBase2Str(i)

        if isPalindrome(binRep):
            palindromes.append(i)

sum = 0
for i in palindromes:
    sum += i

print len(palindromes)
print sum
