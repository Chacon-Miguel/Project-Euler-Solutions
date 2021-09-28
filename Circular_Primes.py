def primes(n):
    if n<=2:
        return []
    sieve=[True]*(n+1)
    for x in range(3,int(n**0.5)+1,2):
        for y in range(3,(n//x)+1,2):
            sieve[(x*y)]=False

    return [2]+[i for i in range(3,n,2) if sieve[i]]
primeNumbs = primes(100)
reversedPrime = 0
accum = 0
for num in primeNumbs:
    if (int(str(num)[::-1])) in primeNumbs:
        print((int(str(num)[::-1])))
        accum += 1
print()
print(accum)