numbers = [2, 1, 2, 6, 1, 3, 6, 2, 4, 3, 5, 8]
uniques = []

for number in numbers:
    if number not in uniques:
        uniques.append(number)

print(numbers)
print(uniques)