mathgrade = float(input('Enter the math grade: '))
physicsgrade = float(input('Enter the physics grade: '))
chemgrade = float(input('Enter the chem grade: '))
no_of_persentclass = float(input('Enter the number of persent: '))
no_of_absentclass = float(input('Enter the absent days: '))

avg_grade = (mathgrade + physicsgrade + chemgrade) / 3
avg_class = (no_of_persentclass - no_of_absentclass) / no_of_persentclass

if (avg_grade >= 0.3):
    if(avg_class >= 0.8):
        print('your grade is: ',avg_grade,  'your total class is: ',avg_class, 'You are pass , congratulations! ')
    else:
            print('your avrage grade is: ',round(avg_grade,3) ,'and your avarge class is: ',round(avg_class,3), 'you are failed ')
else:
    print('you are failed')
