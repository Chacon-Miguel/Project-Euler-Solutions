import math 
# A function to print all prime factors of 
# a given number n 
def primeFactors(n): 
	# Print the number of two's that divide n 
	exponent = 1
	count = 1
	while n % 2 == 0: 
		exponent += 1
		n = n / 2
	# n must be odd at this point 
	# so a skip of 2 ( i = i + 2) can be used 
	for i in range(3,int(math.sqrt(n))+1,2): 
		
		# while i divides n , print i ad divide n 
		while n % i== 0: 
			count += 1
			n = n / i 
		exponent *= count
		count = 1
	# Condition if n is a prime 
	# number greater than 2 
	if n > 2: 
		exponent *= 2
	return exponent
index = 1
count = 2
while primeFactors(index) < 500:
  index += count
  count += 1
print(index)