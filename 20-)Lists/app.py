names = ['John', 'Bob', 'Mosh', "Sarah", 'Mary']
names[0] = 'Jon'
print(names[2:])
print(names)

numbers = [0,6,2,4,5,2,6,12,5,75,123,-2,312,2,3]
holdNum = 0
for i in range(len(numbers)):
    if holdNum < numbers[i]:
        holdNum = numbers[i]
print(f"Largest number is {holdNum}")