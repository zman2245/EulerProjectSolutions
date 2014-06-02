def fact(x):
    n = 1
    prod = n
    while n <= x:
        prod *= n
        n += 1
    return prod

n = 10
results = []
while n < 100000:
    nstr = str(n)

    sum = 0
    for ch in nstr:
        sum += fact(int(ch))

    if sum == n:
        results.append(sum)
        print sum
    n += 1

print results

finalSum = 0
for x in results:
    finalSum += x

print finalSum
