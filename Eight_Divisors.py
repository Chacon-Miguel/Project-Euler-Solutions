import sympy
accum = 0
def primes(n):
    if n<=2:
        return []
    sieve=[True]*(n+1)
    for x in range(3,int(n**0.5)+1,2):
        for y in range(3,(n//x)+1,2):
            sieve[(x*y)]=False
    
    return [2]+[i for i in range(3,n,2) if sieve[i]]
primeNumbs = primes(100)
Max = 0
print(sympy.primepi(100), primeNumbs)  
# for num in primes(52):
#     if num**7 <= 10**12:
#         accum+=1
