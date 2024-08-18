def bubbleSort(array):
    print("Provided array: ")
    print(array)
    length = len(array)
    for i in range(length - 1):
        for j in range(length - 1 - i):
            if array[j] > array[j + 1]:
                array[j], array[j + 1] = array[j + 1], array[j]
    print("Sorted array: ")
    print(array)


l = [9, 12, 10, 4, 3, 15, 2, 6, 14, 5, 7, 8, 11, 16, 13, 1]
bubbleSort(l)
