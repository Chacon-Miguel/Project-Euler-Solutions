# import time
# import sympy
# divisor = 2
# primeFactors = []
# product = 1
# accum = 0
# numb1 = 0
def primes(n):
    if n<=2:
        return []
    sieve=[True]*(n+1)
    for x in range(3,int(n**0.5)+1,2):
        for y in range(3,(n//x)+1,2):
            sieve[(x*y)]=False

    return [2]+[i for i in range(3,n,2) if sieve[i]]
# for numb in sympy.primerange(2, 52):
#     if numb**7 <= 10**12:
#         accum += 1
# numbs = primes(10000)
# accum2 = 0
# for number in numbs:
#     accum += (sympy.primepi(10**12/(number**3))-(numbs.index(number)+1))
# print("two primes:", accum)
# print()
# print('3 distinct primes:', accum2)
# print(time.perf_counter())



# count = 0
# numbs = [12,12, 24, 16, 32, 32, 48, 128, 96, 96, 384]
# for numb in numbs:
#     count += (65437//numb)
# print(count)
# total = 0
# numb_two_Combs = []
# total2 = 0
# 
# for digit in digits:
#     total += (65437//digit)
#     for num in range(digits.index(digit)+1, 4):
#         numb_two_Combs.append(digit*(digits[num]))
#         print(digit, digits[num])
# def combinations(iterable, r):
#     # combinations('ABCD', 2) --> AB AC AD BC BD CD
#     # combinations(range(4), 3) --> 012 013 023 123
#     pool = tuple(iterable)
#     n = len(pool)
#     if r > n:
#         return
#     indices = list(range(r))
#     yield tuple(pool[i] for i in indices)
#     while True:
#         for i in reversed(range(r)):
#             if indices[i] != i + n - r:
#                 break
#         else:
#             return
#         indices[i] += 1
#         for j in range(i+1, r):
#             indices[j] = indices[j-1] + 1
#         yield tuple(pool[i] for i in indices)
# print(combinations([5,8,11,13], 3))
print(len(primes(65437)))