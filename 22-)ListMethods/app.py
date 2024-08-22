num = [5, 2, 1, 7, 4, 8, 5]
#numbers.append(20)
#numbers.insert(0, 10)
'''
numbers.remove(5)
print(numbers)
'''
#numbers.clear()
#numbers.pop()
#print(50 in numbers)
#print(numbers.count(5))
'''
numbers.sort()
print(numbers)
numbers.reverse()
print(numbers)
'''
'''
numbers2 = numbers.copy()
numbers.append(10)

print(f"numbers list :  {numbers}")
print(f"numbers2 list : {numbers2}")
'''

numbers3 = [1, 2, 3, 4, 5, 6, 6, 7, 7, 1, 1, 1, 1]
is_run = True
i = 0
while is_run:
    holdedNum = numbers3[i]
    while numbers3.count(holdedNum) > 1:
        numbers3.remove(holdedNum)
    if i < len(numbers3) -1:
        i += 1
    else:
        is_run = False
print(numbers3)


list1 = [1, 1, 2, 2, 4, 5, 6, 6, 4, 3, 4, 5, 2, 1]
unique = []

for number in list1:
    if unique.count(number) == 0:
        unique.append(number)

