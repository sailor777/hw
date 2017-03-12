#from random import randint
from time import time

biglist = []
biglist_new = []

for val in range(1000000):
    biglist.append(val)

def add_values_for(bigdata):
    bigdata_new = []
    for value in range(len(bigdata)):
        bigdata_new.append(bigdata[value] + 1)
    return bigdata_new

def summa(x):
    return x + 1

# For
start = time()
biglist_new = add_values_for(biglist)
print("Time() add values in big list by for-loop = %s s" % (time() - start))
print("%s" % (30 * '='))

# Map()
start = time()
biglist_new = list(map(summa, biglist))
print("Time() add values in big list by map() = %s s" % (time() - start))
print("%s" % (30 * '='))

# Lambda + map()
start = time()
biglist_new = list(map(lambda x: x + 1, biglist))
print("Time() add values in big list by Lambda & map() = %s s" % (time() - start))
print("%s" % (30 * '='))

# Lambda + filter()
start = time()
biglist_new = list(filter(lambda x: x + 1, biglist))
print("Time() add values in big list by Lambda & filter() = %s s" % (time() - start))
print("%s" % (30 * '='))
