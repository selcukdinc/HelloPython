try:
    age = int(input('Age: '))
    income = 20000
    risk = income / age
    print(age)
except ValueError:
    print('Invalid Value')
except ZeroDivisionError:
    print("Age cannot be 0")

'''
Exit code means
0 - Always successfully worked
other numbers - crash
'''

# Exceptions prevent to program crash