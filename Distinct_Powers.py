sequence = []
for base in range(2, 101):
    for exponent in range(2, 101):
        sequence.append(base**exponent)
print(len(set(sequence)))