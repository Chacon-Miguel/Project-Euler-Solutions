from itertools import combinations
count = 0
product = 1
numbs = []
combs = list(combinations([1,2,3,4,5,6,7,8,9], 5))
combs.sort()
while count != 5:
    for comb in combs:
        for numb in comb:
            product *= numb
        if str(product) == str(comb):
            count += 1
            numbs.append(product)
print(sum(numbs))
