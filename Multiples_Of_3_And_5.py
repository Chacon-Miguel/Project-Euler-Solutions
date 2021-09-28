count = 0
for x in range(3, 1000):
    # If its divisible by three or 5, add it to count
    if not x%3 or not x%5:
        count += x
print(count)