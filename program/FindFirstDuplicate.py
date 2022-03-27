def first_duplicate(array):
    for val in array:
        absValue = abs(val)
        if array[absValue - 1] < 0:
            return absValue
        array[absValue - 1] *= -1
    return -1


array = [2, 1, 5, 2, 3, 3, 4]
print(first_duplicate(array))
