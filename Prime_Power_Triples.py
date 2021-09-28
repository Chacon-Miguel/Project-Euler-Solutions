from Functions import primes
# The greatest possible prime is the square root of 50000000, so find the primes up to that number
P = primes(7072)
# Create a list to store the numbers
count = []
# Iterate through the list to find all possible combinations
for p in P:
    for x in P:
        for y in P:
            # Stop once you go above the limit
            if (p*p + x**3 + y**4) >= 50000000:
                break
            # Add the possible values
            count.append(p*p + x**3 + y**4)
# Convert the list to a set to remove repeating values and then find the length
print(len(set(count)))
