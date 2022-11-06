#QuickSort Jakub Konkol S24406

def quickSort(array, left, right):
    if(left<right):
        q = partition(array, left, right)
        quickSort(array, left, q-1)
        quickSort(array, q+1, right)
        
    
def partition(array, left, right):
    pivot = array[right]
    smaller = left
    for x in range (left,right):
        if(array[x] <= pivot):
            #zamiana elementow ze soba
            array[smaller], array[x] = array[x], array[smaller]
            smaller +=1
    #zamiana elementow ze soba
    array[smaller], array[right] = array[right], array[smaller] 
    return smaller


array = [5,3,7,4,8,6,12,1,9,4,7,8,6]
arrayLenght = len(array)

print("Array at the start: ", array, "\n")
quickSort(array, 0, arrayLenght-1)
print("Sorted array", array)