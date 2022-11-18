# Jakub Konkol S24406
# HeapSort & QuickSort & BubbleSort
import math
import random
import time
import sys

# ta linijka jest dlatego ze jak wywolywalem sortowania
# to dostawalem RecursionError: maximum recursion depth exceeded in comparison
sys.setrecursionlimit(10000)


def msg(message):
    print("\n****************************************************")
    print("\t\t\t", message)
    print("****************************************************")

#generowanie wielkiej tablicy z losowymi liczbami
def giveMeHugeArray():
    array = []
    numberOfElements = random.randint(100000, 1000000)
    for x in range(0, numberOfElements):
        array.append(random.randint(0, 5000))
    return array
#generowanie malej tablicy w ramach testu
def giveMeSmallArray():
    array = []
    numberOfElements = random.randint(10, 1000)
    for x in range(0, numberOfElements):
        array.append(random.randint(0, 100))
    return array

################################################QuickSort###############################################################
def quickSort(array, left, right):
    if left < right:
        q = partition(array, left, right)
        quickSort(array, left, q - 1)
        quickSort(array, q + 1, right)
    return array


def partition(array, left, right):
    pivot = array[right]
    # pivot = (array[right] + array[left]) / 2
    smaller = left
    for x in range(left, right):
        if array[x] <= pivot:
            array[smaller], array[x] = array[x], array[smaller]
            smaller += 1
    array[smaller], array[right] = array[right], array[smaller]
    return smaller

################################################HeapSort################################################################
def heapSort(array):
    n = len(array)
    for i in range(n//2 -1, -1, -1):
        heapify(array, n, i)
    for i in range(n-1, 0, -1):
        array[i], array[0] = array[0], array[i]
        heapify(array, i, 0)
    return array

def heapify(array, n, i):
    largest = i
    left = 2 * i
    right = 2 * i + 1
    if left < n and array[i] < array[left]:
        largest = left
    if right < n and array[largest] < array[right]:
        largest = right
    if largest != i:
        array[i], array[largest] = array[largest], array[i]
        heapify(array, n, largest)

################################################BubbleSort##############################################################
def bubbleSort(array):
    n = len(array)
    for i in range(n):
        for j in range(0, n-i-1):
            if array[j] > array[j+1]:
                array[j], array[j+1] = array[j+1], array[j]
    return array
########################################################################################################################
# arrayToSort = giveMeHugeArray()
arrayToSort = giveMeSmallArray()
arrayLenght = len(arrayToSort)


# QuickSort
t = time.process_time()
sortedArray = quickSort(arrayToSort, 0, arrayLenght-1)
qs_execution_time = time.process_time() - t
print(sortedArray)

t = time.process_time()
quickSort(sortedArray, 0, arrayLenght-1)
qs2_execution_time = time.process_time() - t

sortedArray.reverse()
t = time.process_time()
quickSort(sortedArray, 0, arrayLenght-1)
qs3_execution_time = time.process_time() - t

# HeapSort
t = time.process_time()
sortedArray = heapSort(arrayToSort)
hs_execution_time = time.process_time() - t
print(sortedArray)

t = time.process_time()
heapSort(sortedArray)
hs2_execution_time = time.process_time() - t

sortedArray.reverse()
t = time.process_time()
heapSort(sortedArray)
hs3_execution_time = time.process_time() - t

#BubbleSort
t = time.process_time()
sortedArray = bubbleSort(arrayToSort)
bs_execution_time = time.process_time() - t
print(sortedArray)

t = time.process_time()
bubbleSort(sortedArray)
bs2_execution_time = time.process_time() - t

sortedArray.reverse()
t = time.process_time()
bubbleSort(sortedArray)
bs3_execution_time = time.process_time() - t

msg("QuickSort")
print("Czas pierwszego sortowania (pierwotna tablica): ", qs_execution_time, "s")
print("Czas drugiego sortowania (tablica posortowana): ", qs2_execution_time, "s")
print("Czas trzeciego sortowania (tablica posortowana odwrócona): ", qs3_execution_time, "s")
print("ilosc elementów w tablicy: ", arrayLenght)
msg("HeapSort")
print("Czas pierwszego sortowania (pierwotna tablica): ", hs_execution_time, "s")
print("Czas drugiego sortowania (tablica posortowana): ", hs2_execution_time, "s")
print("Czas trzeciego sortowania (tablica posortowana odwrócona): ", hs3_execution_time, "s")
print("ilosc elementów w tablicy: ", arrayLenght)
msg("bubbleSort")
print("Czas pierwszego sortowania (pierwotna tablica): ", bs_execution_time, "s")
print("Czas drugiego sortowania (tablica posortowana): ", bs2_execution_time, "s")
print("Czas trzeciego sortowania (tablica posortowana odwrócona): ", bs3_execution_time, "s")
print("ilosc elementów w tablicy: ", arrayLenght)
