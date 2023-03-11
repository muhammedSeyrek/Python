import random
array = [[random.randint(1, 9) for x in range(9)] for y in range(9)]
for i in range(len(array)):
    for j in range(len(array[i])):
        print("{:<2}".format(array[i][j]), end=" ")
    print()