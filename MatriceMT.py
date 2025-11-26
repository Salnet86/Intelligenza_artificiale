array = [
    [1, 2, 3],
    [3, 4, 5],
    [5, 6, 7]
]

for i in range(len(array)):
    for j in range(i + 1, len(array)):  # parte da i+1
        temp = array[i][j]
        array[i][j] = array[j][i]
        array[j][i] = temp

#print(array)


for matrice in array:
    print(matrice)


