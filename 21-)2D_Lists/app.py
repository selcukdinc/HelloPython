'''
x_length = 3
y_length = 3
plotter = 1
for i in range(3):
    row_cache = ""
    for j in range(y_length):
        row_cache += f"{plotter} "
        plotter += 1
    print(row_cache)
'''
def print_matrix(array_list):
    for i in range(len(array_list)):
        row_cac = ""
        for j in range(len(array_list[0])):
            row_cac += f"{array_list[i][j]} "
        print(row_cac)


matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9],
    [7, 8, 9]
]

print(matrix[0][1])
print_matrix(matrix)