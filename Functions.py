import math
def primes(n):
    if n<=2:
        return []
    sieve=[True]*(n+1)
    for x in range(3,int(n**0.5)+1,2):
        for y in range(3,(n//x)+1,2):
            sieve[(x*y)]=False

    return [2]+[i for i in range(3,n,2) if sieve[i]]
def primeFactors(n): 
	"""Returns a list of all prime factors. Example: [2, 2, 2, 3] for 24"""
	# Print the number of two's that divide n 
	
	factors = []
	while n % 2 == 0: 
		n = n / 2
		factors.append(2)
	# n must be odd at this point 
	# so a skip of 2 ( i = i + 2) can be used 
	for i in range(3,int(math.sqrt(n))+1,2): 
		
		# while i divides n , print i ad divide n 
		while n % i== 0: 
			n = n / i 
			factors.append(i)
	# Condition if n is a prime 
	# number greater than 2 
	if n > 2: 
		factors.append(n)
	return factors
def primeFactorAmount(n): 
	"""Returns how many prime factors some n number has. Example: 1 for n = 4"""
	# Print the number of two's that divide n 
	
	count = 0
	while n % 2 == 0: 
		n = n / 2
		count += 1
	# n must be odd at this point 
	# so a skip of 2 ( i = i + 2) can be used 
	for i in range(3,int(math.sqrt(n))+1,2): 
		
		# while i divides n , print i ad divide n 
		while n % i== 0: 
			n = n / i 
			count += 1
	# Condition if n is a prime 
	# number greater than 2 
	if n > 2: 
		count += 1
	return count