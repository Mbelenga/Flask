number = input("Please input an integer. ")

if (number.isnumeric()):
    number = int(number)
    if (number > 20):
        print("Your input: " + str(number) + " > 20")
    if (number > 10):
        print("Your input: " + str(number) + " > 10")
    if (number > 0):
        print("Your input: " + str(number) + " > 0")
else:
    print("Your input is not an integer or it's negative.")