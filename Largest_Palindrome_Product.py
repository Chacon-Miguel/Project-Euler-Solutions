largestPal = 0
possiblePal =0
for number in range(100, 1000):
    for numb in range(100, 1000):
        possiblePal = str(number*numb)
        if possiblePal == possiblePal[::-1] and number*numb > largestPal:
            largestPal = number*numb
print(largestPal)