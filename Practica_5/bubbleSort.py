def bubbleSort(listaN):
    n = len(listaN)
    for i in range(n):
        for j in range(0, n-i-1):
            if listaN[j] > listaN[j+1]:
                listaN[j], listaN[j+1] = listaN[j+1], listaN[j]
    return listaN

def selectionSort(listaN):
    n = len(listaN)
    for i in range(n):
        min_idx = i
        for j in range(i+1, n):
            if listaN[j] < listaN[min_idx]:
                min_idx = j
        listaN[i], listaN[min_idx] = listaN[min_idx], listaN[i]
    return listaN

def insertionSort(listaN):
    n = len(listaN)
    for i in range(1, n):
        key = listaN[i]
        j = i - 1
        while j >= 0 and key < listaN[j]:
            listaN[j + 1] = listaN[j]
            j -= 1
        listaN[j + 1] = key
    return listaN

def mergeSort(listaN):
    if len(listaN) > 1:
        mid = len(listaN) // 2
        L = listaN[:mid]
        R = listaN[mid:]

        mergeSort(L)
        mergeSort(R)

        i = j = k = 0

        while i < len(L) and j < len(R):
            if L[i] < R[j]:
                listaN[k] = L[i]
                i += 1
            else:
                listaN[k] = R[j]
                j += 1
            k += 1

        while i < len(L):
            listaN[k] = L[i]
            i += 1
            k += 1

        while j < len(R):
            listaN[k] = R[j]
            j += 1
            k += 1
    return listaN

def quickSort(listaN):
    if len(listaN) <= 1:
        return listaN
    else:
        pivot = listaN[0]
        less_than_pivot = [x for x in listaN[1:] if x < pivot]
        greater_than_pivot = [x for x in listaN[1:] if x >= pivot]
        return quickSort(less_than_pivot) + [pivot] + quickSort(greater_than_pivot)

def countingSort(listaN):
    max_val = max(listaN)
    count = [0] * (max_val + 1)
    output = [0] * len(listaN)

    for num in listaN:
        count[num] += 1

    for i in range(1, len(count)):
        count[i] += count[i - 1]

    for num in reversed(listaN):
        output[count[num] - 1] = num
        count[num] -= 1

    return output

listaN = [10, 50, 23, 3, 43, 23, 29, 49, 12, 40]

'''
print("Lista original:", listaN)
sorted_list = bubbleSort(listaN)

print("Lista ordenada (-----Bubble Sort-----):", sorted_list)

sorted_list = selectionSort(listaN)
print("Lista ordenada (-----Selection Sort-----):", sorted_list)

sorted_list = insertionSort(listaN)
print("Lista ordenada (-----Insertion Sort-----):", sorted_list)

sorted_list = mergeSort(listaN)
print("Lista ordenada (-----Merge Sort-----):", sorted_list)


sorted_list = quickSort(listaN)
print("Lista ordenada (-----Quick Sort-----):", sorted_list)

'''

sorted_list = countingSort(listaN)
print("Lista ordenada (-----Counting Sort-----):", sorted_list)