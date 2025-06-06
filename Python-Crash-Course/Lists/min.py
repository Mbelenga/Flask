numbers = [5, 3, 8, -1, 2.2,0]

min_number = numbers[0]

for number in numbers:
    if number < min_number:
        min_number = number
print(min_number, "is the min_number")