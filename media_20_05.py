counter = 0
grades = []
average = 0
while True:
    grade = input('Type the student grade: ')

    if grade == 'exit':
        print(f'The average is: {average}')
        break
    
    if not grade.isdigit():
        print('Invalid grade!')
        continue

    float_grade = float(grade)

    if float_grade < 0 or float_grade > 10:
        print('Grade must be between 0 and 10')
        continue

    grades.append(float_grade)

    counter += 1

    sum_grades = sum(grades)

    average = sum_grades / counter