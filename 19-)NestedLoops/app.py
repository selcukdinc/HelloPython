'''
for x in range(4):
    for y in range(3):
        print(f"({x}, {y})")
'''
'''
numbers_list = [5, 2, 5, 2, 2]
for i in range(len(numbers_list)):
    x_cache = ""
    for j in range(numbers_list[i]):
        x_cache += "X"
    print(x_cache)
'''

def bigger_letter(listnum):
    for z in range(len(listnum)):
        y_cache = ""
        for j in range(listnum[z]):
            y_cache += "X"
        print(y_cache)

L = [2,2,2,2,5]
bigger_letter(L)