
# Bubble sort


def bubbleSort(ls):
    for step in range(len(ls) - 1):
        for i in range(len(ls) - 1 - step):
            a = ls[i]
            b = ls[i + 1]  # element next to i
            if a > b:
                # if a is greater then b, swap them
                ls[i + 1] = a
                ls[i] = b
    return ls

# Insertion sort


def insertionSort(ls):
    for index in range(1, len(ls)):
       for insertionIndex in range(index, 0 , -1):
           a = ls[insertionIndex -1]
           b = ls[insertionIndex]

           if a <= b:
               break

           ls[insertionIndex] = a
           ls[insertionIndex - 1] = b
    return ls

