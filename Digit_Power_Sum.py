def sum_of_digits(n):
    return sum(map(int, str(n)))

a = []
bases = []
n = 30
for b in range(2, 190):
    for e in range(2, 10):
        if sum(map(int, str(b**e))) == b:
            a.append(b**e)
            bases.append(b)

a.sort()
print(a[29])