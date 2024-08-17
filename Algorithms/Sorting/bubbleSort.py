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


l = [1, 10, 4, 3, 2, 6, 5, 7, 8, 11, 16, 13, 12]
bubbleSort(l)
