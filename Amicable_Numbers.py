from Functions import primes
from itertools import permutations
a = list(permutations(range(10, 4)))
b = primes(10**5)
for f in a:
    if f in b:
        print(f)
