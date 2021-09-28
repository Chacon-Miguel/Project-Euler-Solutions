# importing the required module 
import timeit 

# code snippet to be executed only once 
# code snippet whose execution time is to be measured 
mycode = ''' 
accum = 0
def primes(n):
    if n<=2:
        return []
    sieve=[True]*(n+1)
    for x in range(3,int(n**0.5)+1,2):
        for y in range(3,(n//x)+1,2):
            sieve[(x*y)]=False
    
    return [2]+[i for i in range(3,n,2) if sieve[i]]

for num in primes(52):
    if num**7 <= 10**12:
        accum+=1
'''

# timeit statement 
print (timeit.timeit(setup="pass", stmt = mycode, number = 10000))
