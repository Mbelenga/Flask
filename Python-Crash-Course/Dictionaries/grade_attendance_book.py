Billy = {
    'name' : 'Billy',
    'Grades': [80, 69, 75, 96, 82],
    'attendance' : [True, True, True, True, True],
}

Sarah = {
    'name': 'Sarah',
    'grades': [10, 72, 17, 79, 88],
    'attendance' : [True, False, True, False, True]
}

Ben = {
    'name': 'Ben',
    'grades': [66, 69, 77, 85, 90],
    'attendance' : [False, False, False, False, False]
}

students = {'1': Billy, '2': Sarah, '3': Ben}
# get number of students
print(len(students)) # number of keys

print(students.keys())

# iterate
for k in students:
    print('key:', k)

# get billy's attendance
Billy = students['1']
print(Billy['attendance'])