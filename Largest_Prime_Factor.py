divisor = 2
numb = 13195%2
while numb != 0:
    for num1 in range(2, divisor):
        if divisor%num1 == 0:
            numb = numb%divisor
    divisor += 1
print(divisor)
