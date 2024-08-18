def selectionSort(array):
    length = len(array)

    for i in range(length - 1):
        min_index = i
        for j in range(i + 1, length):
            if array[j] < array[min_index]:
                min_index = j
        array[i], array[min_index] = array[min_index], array[i]

    print(array)


l = [9, 12, 10, 4, 3, 15, 2, 6, 14, 5, 7, 8, 11, 16, 13, 1]
selectionSort(l)
