# A unit fraction contains 1 in the numerator. The decimal representation of the unit fractions with denominators 2 to 10 are given:
# 
# 1/2 =   0.5
# 1/3 =   0.(3)
# 1/4 =   0.25
# 1/5 =   0.2
# 1/6 =   0.1(6)
# 1/7 =   0.(142857)
# 1/8 =   0.125
# 1/9 =   0.(1)
# 1/10    =   0.1
# Where 0.1(6) means 0.166666..., and has a 1-digit recurring cycle. It can be seen that 1/7 has a 6-digit recurring cycle.
# 
# Find the value of d  1000 for which 1/d contains the longest recurring cycle in its decimal fraction part.

max_cycle   = 0
answer      = 1

for d in range(1,1001):
    rem = 1
    remainders = []

    for dd in range(1, d+1):
        if rem in remainders:
            index = len(remainders) - 1
            cycle_len = 1
            while remainders[index] != rem:
                cycle_len += 1
                index -= 1

            if cycle_len > max_cycle:
                max_cycle = cycle_len
                answer    = d

            break

        remainders.append(rem)
        rem = (rem*10) % d
        if rem == 0:
            break

    
print "max cycle:", max_cycle
print "answer:", answer
