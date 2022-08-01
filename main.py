from itertools import permutations
import datetime, time
import math

l = range(40)

i = 0
N = 10
start_time = time.time()

for c in permutations(l, 12):
    i+=1
    # print(c)
    if i == N: break

# t = time.time() - start_time
# print("--- %s seconds ---" % (t))

# n_combs = math.factorial(40)/(math.factorial(12)*math.factorial(40-12))
# total_time = n_combs * t / N
# print(datetime.timedelta(seconds = total_time))

def unique_permutations(iterable, r=None):
    # https://stackoverflow.com/questions/6284396/permutations-with-unique-values
    previous = tuple()
    for p in permutations(sorted(iterable), r):
        if p > previous:
            previous = p
            yield p

combs = []
for p in unique_permutations('123'*4, 12):
    print(p)
    combs.append(p)

print(len(combs))

'''
numero di possibili modi per disporre le carte che prendono nel mazzo
N1 = 40! /( 12! * (40-12)! ) = 5586853480

numero di permutazioni distinte per ordinare le 12 carte che prendono
N2 = 34650

numero di mazzi distini
N = 193584473082000 = 1.9358e+14

'''