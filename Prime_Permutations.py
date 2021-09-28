from Functions import primes
from itertools import permutations
a = permutations(list(str(1487)), 4)
print(a)
# a = primes(10**4)
# a = a[len(primes(10**3)):]
# sequence = ''
# count = 0
# for numb in a:
#     q = permutations(str(numb), 4)
#     for perm in q:
#         if perm in numb:
#             count = 0
#     if count == 2:
#         sequence = sequence + str(perm)
# print(sequence)