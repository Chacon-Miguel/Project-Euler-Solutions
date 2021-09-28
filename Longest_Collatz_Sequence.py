Collatz = {1:1}
longestChain = 0
answer = -1
def countChain(n):
    if n in Collatz:
        return Collatz[n]
    if not n%2:
        Collatz[n] = 1 + countChain(n/2)
    else:
        Collatz[n] = 2 + countChain((3*n+1)/2)
    return Collatz[n]
for number in range(500000, 1000000):
    if countChain(number) > longestChain:
        longestChain = countChain(number)
        answer = number
print(answer)