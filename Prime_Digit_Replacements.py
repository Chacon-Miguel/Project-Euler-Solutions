from Functions import primes
a = primes(1000000)
family = []
for prime in a:
    if len(str(prime)) - len(set(str(prime))) == 5:
        family.append(prime)
    if len(family) == 8:
        break
print(family[0])