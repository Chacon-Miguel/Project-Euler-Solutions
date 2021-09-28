fibs = [1, 1]
while fibs[-1] < 4000000:
    fibs.append(fibs[-1]+fibs[-2])
print(sum(fibs[2::3]))