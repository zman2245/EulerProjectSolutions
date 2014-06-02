from AbundantNumbers import getDivisors
from AbundantNumbers import getAbundantNumbers

startnum = 28123


numbers = getAbundantNumbers(startnum)
print len(numbers)

print "Got the numbers..."

# build the set of all numbers covered
sumset = []
size = len(numbers)
i = 0
while i < size:
    j = i
    while j < size:
        x = numbers[i]
        y = numbers[j]
        print x, y
        if (x + y > startnum):
            j += 1
            continue

        if ((x + y) not in sumset):
            sumset.append(x + y)
        j += 1
    i += 1

# total sum of 1...28123
totalsum = 0
for x in range(startnum + 1):
    totalsum += x
print "totalsum", totalsum, sumset
for x in sumset:
    totalsum -= x

print totalsum


exit(1)
marked = 0
i = 1
while i < 28123:
    print i
    for x in numbers:
        for y in numbers:
            if (x + y == i):
                marked = 1
                break

        if marked == 1:
            break

    if marked != 1:
        results.append(i)

    marked = 0
    i += 1


print results


sum = 0
for j in results:
    sum += j

print sum
