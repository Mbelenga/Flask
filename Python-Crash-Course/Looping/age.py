age = int(input('Enter your age? '))
if age == 0:
    print("Seriously?")
elif age < 100:
    print("In", 100 - age, "years you will be 100 years old")
elif age == 100:
    print("you are", age, "years old")
else:
    print("Acentury and going strong!")