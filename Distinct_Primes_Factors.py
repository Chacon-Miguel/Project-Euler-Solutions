import sympy
primeFactors = []
accum = 0
numb = 14
prevNumb = 3
while accum != 2:
    for x in range(numb, numb+2):
        if len(sympy.primefactors(numb)) == 2:        
            accum += 1
            primeFactors.append(numb)
            continue
        else:
            break
    numb += 1
    print(numb)
